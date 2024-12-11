from tools.echobot import robot_send_message
from tools.standard_log import log_to_file
import akshare as ak


def baffe_index_process(years, data):
    # data = pd.DataFrame(all_baffe_index['data'])
    data['baffe_index'] = data['总市值']/data['GDP']
    baffe_index_25 = data['baffe_index'][-365*years:].quantile(0.25)
    baffe_index_50 = data['baffe_index'][-365*years:].quantile(0.5)
    baffe_index_75 = data['baffe_index'][-365*years:].quantile(0.75)
    return baffe_index_25, baffe_index_50, baffe_index_75


@log_to_file
def legu_main():
    # 获取巴菲特指数, 并判断目前高估还是低估
    all_baffe_index = ak.stock_buffett_index_lg()
    all_baffe_index.to_csv('./data/stock_buffett_index.csv')
    buffet_index = all_baffe_index.iloc[-1,2]/all_baffe_index.iloc[-1,3]
    baffe_index_525, baffe_index_550, baffe_index_575 = baffe_index_process(
        5, all_baffe_index)
    baffe_index_125, baffe_index_150, baffe_index_175 = baffe_index_process(
        1, all_baffe_index)
    message = f"""
今日巴菲特指数:                            {buffet_index:.2%}
最近1年巴菲特指数上四分位:      {baffe_index_175:.2%}
最近1年巴菲特指数均值:              {baffe_index_150:.2%}
最近1年巴菲特指数下四分位:      {baffe_index_125:.2%}
最近5年巴菲特指数上四分位:      {baffe_index_575:.2%}
最近5年巴菲特指数均值:              {baffe_index_550:.2%}
最近5年巴菲特指数下四分位:      {baffe_index_525:.2%}"""
    robot_send_message(message)
    return message
