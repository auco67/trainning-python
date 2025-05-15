import datetime
import os
from pathlib import Path
import pandas as pd

from lib.common import get_last_month
from lib.filepath import filepath
from lib.plan_master import PlanMaster

class PlanProgress:
    """
    プラン推移に関する処理
        各自治体のプラン（基本プラン/応援プラン）を年度月に記述した一覧を作成する
    """
    def __init__(self) -> None:
        """
        Description:
            プラン推移クラスのインスタンス
        
        Property:
            plan_progress_dir(str): プラン推移格納フォルダパス
            plan_progress_excel(str): プラン推移Excelファイルパス
            df_plan_master(pd.DataFrame): プラン判定マスタDataFrame
            df_plan_progress(pd.DataFrame): プラン推移DataFrame
        """
        self.plan_progress_dir: str = os.getenv('MASTER_SAVE_DIR')
        self.plan_progress_excel: str = Path(self.plan_progress_dir) / "plan_progress.xlsx"
        self.df_plan_master: pd.DataFrame = PlanMaster(file_path=filepath.get('PLAN_MASTER')).df.fillna("")
        self.df_plan_progress: pd.DataFrame = None
    
    def is_xl(self) -> bool:
        """指定されたExcelファイルの存在チェック

        Returns:
            bool: 存在する True / 存在しない False
        """
        if not os.path.exists(self.plan_progress_excel):
            return False
        return True
    
    def _generate_master_dir(self,file_name:str) -> str:
        """プラン判定マスタファイルパスを計算する

        Args:
            file_name (str): プラン判定マスタのファイル名

        Returns:
            (str) : ファイルパス
        """
        return self.plan_progress_dir + '/' + file_name
    
    def _get_dict_month_of_year(self) -> dict[str,str]:
        """年度の月の辞書を返す

        Returns:
            dict[str,str]: 年度の月の辞書
        """
        this_year = datetime.datetime.now().year
        next_year = this_year + 1
        year_month = ["Apr.", "May", "Jun.","Jul.","Aug.","Sep.","Oct.","Nov.","Dec.","Jan.","Feb.","Mar."]
        month_of_year = {}
        counter = 4
        for month in year_month:
            if month != "Jan.":
                if month != "Feb." and month != "Mar.":
                    month_of_year[month] = f"{this_year}-{counter:02}"
                else:
                    month_of_year[month] = f"{next_year}-{counter:02}"
                counter +=1
            if month == "Jan.":
                counter = 1
                month_of_year[month] = f"{next_year}-{counter:02}"
                counter +=1
        return month_of_year
    
    def create_plan_progress(self):
        """プラン推移を作成する"""
        df_plan_master = self.df_plan_master.drop(columns="プラン名")
        month_of_year:dict[str, str] = self._get_dict_month_of_year()
        
        for key, value in month_of_year.items():
            df_plan_master[value] = ""
        
        df_plan_master = df_plan_master.fillna("")
        df_plan_master.to_excel(self.plan_progress_excel, index=False)
        
    def _get_plan_progress_xlsx_to_df(self) -> pd.DataFrame:
        """プラン推移ファイルを読み込みDataFrameを返す

        Returns:
            pd.DataFrame: ファイル推移のDataFrame
        """
        return pd.read_excel(self.plan_progress_excel, dtype='object').infer_objects(copy=False)
    
    def _get_df_plan_master(self) -> pd.DataFrame:
        """プラン判定マスタをDataFrameで返す

        Returns:
            pd.DataFrame: プラン判定マスタのDataFrame
        """
        return self.df_plan_master
    
    def merge_master_and_progress(self) -> pd.DataFrame:
        """プラン推移とプラン判定マスタを自治体ID、自治体名でマージする


        Returns:
            pd.DataFrame: マージ後のDataFrame
        """
        df_plan_progress = self._get_plan_progress_xlsx_to_df()
        df_plan_master = self._get_df_plan_master()
        
        # df_plan_progressにdf_plan_masterをマージする
        return pd.merge(left=df_plan_progress, right=df_plan_master, how="left", on=["自治体ID", "自治体名"]).fillna("")
    
    def column_sorting_after_merge(self, df_merge: pd.DataFrame, last_month:str) -> None:
        """マージ後DataFrameの列を並び替えする

        Args:
            df_merge (pd.DataFrame): 並び替え前のDataFrame
            last_month (str): 先月文字列 yyyy-mm
        """
        # 列名「プラン名」を変更
        df_merge = df_merge.rename(columns={"プラン名":f"{last_month}_x"})

        # 列項目をリストで取得
        columns = df_merge.columns.to_list()
        
        # 並び替え元の列項目の列番号を取得
        target_source_col = df_merge.columns.get_loc(f"{last_month}_x")
        
        # 並び替え先の列項目の列番号を取得
        target_destination_col = df_merge.columns.get_loc(last_month)

        # 列名変更（元列項目名に先列項目名を、先列項目名に元列項目名を設定）
        columns[target_destination_col] = f"{last_month}_x"
        columns[target_source_col] = last_month
        
        # 列項目リストでDataFrameを並び替える
        df_merge = df_merge.reindex(columns=columns)

        # 不要になった列を削除
        df_merge = df_merge.drop(columns=last_month)
        
        # 列項目名を変更
        df_merge = df_merge.rename(columns={f"{last_month}_x":last_month})

        self.df_plan_progress = df_merge
    
    def to_excel(self) -> None:
        """プラン推移のDataFrameをExcel出力する

        Args:
            last_month (str): 先月文字列 yyyy-mm
        """
        self.df_plan_progress.to_excel(self.plan_progress_excel, index=False)
    
if __name__ == "__main__":
    
    # PlanProgressクラスの初期化
    plan_progress = PlanProgress()
    
    # プラン推移Excelファイルの存在確認
    if not plan_progress.is_xl():
        
        # プラン推移Excelファイルを新規作成する
        plan_progress.create_plan_progress()
    
    # プラン推移とプラン判定マスタを自治体ID、自治体名でマージする
    df_merge = plan_progress.merge_master_and_progress()
    
    # 先月文字列をyyyy-mm形式に設定
    last_month = get_last_month("yyyymm")
    last_month = f"{last_month[:4]}-{int(last_month[-2:]):02}"
    
    # マージ後のDataFrameを列並び替えする
    plan_progress.column_sorting_after_merge(df_merge=df_merge,last_month=last_month)
    
    # プラン推移Excelファイルを出力する
    plan_progress.to_excel()