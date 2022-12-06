# Yellow-Bull

## Abstract
以 Telegram bot 追蹤 [DC View](http://market.dcview.com/) 二手市場上的最新產品。
> 簡易版，僅對單一使用者發布追蹤訊息。
> 直接訂閱現有[頻道](https://t.me/+XJmAfKkrRsQwYzll)，目前追蹤 Fujifilm 和 Sony。

## 前置作業
1. 去 Telegram 找 @BotFather 申請一個 Bot。
    1. 輸入名稱
    2. 輸入 username
    3. 記下 token
2. 去跟你的 bot 對話。
> 可以透過創立 channel 來達成群發效果。
3. 瀏覽器打開 (https://api.telegram.org/bot\<Your bot token>/getUpdates)，可以找到你剛剛的對話及你自己的 id。

## 環境變數
| Name         | Desc                                      | Example                                        |
| ------------ | ----------------------------------------- | ---------------------------------------------- |
| TG_TOKEN     | 取得的 bot token  (前置作業步驟 1 取得)   | 1089050203:AAGmvyQmtyDf2kfXXX8xXXxxx_23X-Xxx6X |
| TG_CHAT_ID   | 要發送對象的 ID (前置作業步驟 3 取得)     | 1001623472781                                  |
| YB_TRACK_INT | 追蹤間隔                                  | 10                                             |
| YB_BRANDS    | 追蹤品牌，用 ',' 分隔                     | Sony,Fujifilm                                  |

## 使用設定檔
* command
    ```bash
    python ./YellowBull.py --use_config
    ```
* botConfig.json
    ```json
    {
        "TG_TOKEN": "TBD",
        "TG_CHAT_ID": "TBD",
        "YB_TRACK_INT": 30,
        "YB_BRANDS": [
            "Sony",
            "Fujifilm"
        ]
    }
    ```

## Docker 建置命令
```bash
docker build . -t yoyo860224/yellow-bull
```

## 提供 Fly.io 部署
```bash
flyctl launch --image yoyo860224/yellow-bull:latest --name yellow-bull
```
