import baostock as bs
import pandas as pd
from tools.standard_log import log_to_file


@log_to_file
def get_stock_data(code="sh.600000", start_date='2017-07-01', end_date='2017-12-31', save_path='history_A_stock_k_data.csv'):
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    error_info = {}
    error_info['login respond error_code'] = lg.error_code
    error_info['login respond error_msg'] = lg.error_msg

    #### 获取沪深A股历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。“分钟线”不包含指数。
    # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
    rs = bs.query_history_k_data_plus(code,
                                      "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                      start_date=start_date, end_date=end_date,
                                      frequency="d", adjustflag="3")

    error_info['query_history_k_data_plus respond error_code'] = rs.error_code
    error_info['query_history_k_data_plus respond  error_msg'] = rs.error_msg

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 结果集输出到csv文件 ####
    result.to_csv(f"./data/{save_path}", index=False)

    #### 登出系统 ####
    bs.logout()
    return result, error_info


if __name__ == '__main__':
    get_stock_data(
        code="sh.000300",
        start_date="2020-01-01",
        end_date="2020-01-02",
        save_path="history_A_stock_k_data.csv"
    )
