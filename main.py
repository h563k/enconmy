from tools.stocks import get_stock_data
from tools.echobot import robot_send_message

if __name__ == '__main__':
    get_stock_data(
        code="sh.000300",
        start_date="2020-01-01",
        end_date="2020-01-02",
        save_path="history_A_stock_k_data.csv"
    )
    