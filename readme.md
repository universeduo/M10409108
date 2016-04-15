# 巨量資料分析HW1_M10409108

#### Data來源 

---
  使用的API
  > TwitterAPI

  內容主題
  > 演員
  
  下哪個查詢字串
  > #RobinWilliams

##### 收集到的 Data Format(JSON的欄位架構）
　
```
 *  "text": 文字內容
 *  "source": 
 *  "id_str": 這篇Tweet的ID
 *  "place": 該Tweet是否有與某地連結
 *  "coordinates": 這篇Tweet的發文座標
 *  "created_at": 使用者發出Tweet的時間
 *  "is_quote_status": 是否在被引用的狀態
 *  "retweet_count": 這篇Tweet被轉發的次數
 *  "favorite_count": 這篇Tweet有多少個喜歡
 *  "lang": 根據機器偵測自動判斷出該Tweet的語言
 *  "geo": 不贊同使用，現在都使用coordinates欄位紀錄
 *  "retweeted": 這篇Tweet是否有被其他Twitter使用者轉發
 *  "favorited": 這篇Tweet是否有被其他已驗證的使用者按喜歡
 *  "truncated": tweet內容是否有被裁切掉，若超過140字會被切掉
 *  "contributors": 使用者物件的集合，象徵幫助Tweet的人，代表官方tweet創辦人
 *  "id":這篇Tweet的ID（以整數表示），數字會大於53bit造成有些程式語言難以解譯
 *  "in_reply_to_status_id": 若這篇Tweet為回覆別人的Tweet才會顯示被回覆的Tweet的ID（以整數表示）
 *  "in_reply_to_user_id_str": 若這篇Tweet為回覆別人的Tweet，會顯示被回覆的Tweet的作者ID（以字串表示）
 *  "in_reply_to_status_id_str": 若這篇Tweet為回覆別人的Tweet，會顯示被回覆的Tweet的ID（以字串表示）
 *  "in_reply_to_screen_name": 可為空值，若這篇Tweet為回覆別人的Tweet，會顯示原Tweet名稱
 *  "in_reply_to_user_id": 可為空值，若這篇Tweet為回覆別人的Tweet，會顯示原Tweet的使用者ID（以整數表示）
 *  "metadata": 
    * "iso_language_code": 該網站使用的語系
    * "result_type": Tweet的型態為何，是熱門Tweet還是近期所發出的Tweet
 *  "entities": 
    * "user_mentions": 有無提到其他的Twitter使用者
    * "hashtags": 被解析出來的標籤
    * "urls": 包含在這篇Tweet裡面的網址
 *  "user": 
    * "follow_request_sent": 可為空值，是否有已驗證的使用者要求追蹤受到保護的使用者帳戶
    * "has_extended_profile": 有沒有擴展的profile
    * "profile_use_background_image": 使用者是否同意可以使用他們上傳的背景圖片
    * "id": 使用者的ID（以整數表示），數字會大於53bit造成有些程式語言難以解譯
    * "profile_text_color": 使用者使用的的字體顏色（十六進位）
    * "profile_sidebar_fill_color": 使用者使用的側邊欄位的背景顏色（十六進位）
    * "entities": Entity會提供metadata及額外關於這篇Tweet的相關資訊
       * "description": 
          * "urls": 這篇Tweet涵蓋的網址
    * "profile_sidebar_border_color": 使用者使用的側邊欄位的邊框顏色（十六進位）
    * "id_str": 使用者（以字串表示）
    * "profile_background_color": 使用者使用的的背景顏色（十六進位）
    * "listed_count": 使用者擁有的list數量
    * "is_translation_enabled": 使用者是不是允許翻譯
    * "utc_offset": 與GMT標準時間的時差（以秒顯示）
    * "statuses_count": 使用者發出的Tweet數量
    * "description": 使用者自介
    * "friends_count": 使用者追蹤其他使用者的數量
    * "profile_link_color": 使用者使用的的連結顏色（十六進位）
    * "profile_image_url":使用者照片的網址（基於HTTP）
    * "following": 使用者是否有被其他已驗證的使用者追蹤
    * "geo_enabled": 使用者是否同意將地理位置顯示於照片上
```
