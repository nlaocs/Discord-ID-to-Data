import base64
import datetime

while True:
    userid = input("ユーザーIDかチャンネルIDを入力してください: ")
    if userid == None:
        print("IDが入力されていないか、機能していません")
        continue
    try:
        floatid = float(userid)
    except:
        print("IDが機能していません")
        continue
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    datenum = (floatid / 4194304) + 1420070400000
    time = datetime.datetime.utcfromtimestamp(datenum/1000.0)
    timejst = datetime.datetime.fromtimestamp(datenum/1000.0)
    print(f"\nトークン: " + encodedStr.replace("=", "") + ".****.********")
    print("作成日時(JST) : " + timejst.strftime('%Y-%m-%d %H:%M:%S'))
    print("作成日時(UTC): " + time.strftime('%Y-%m-%d %H:%M:%S'))
    print(f"作成日時UNIXタイムスタンプ(秒): {datenum/1000}")
    print(f"作成日時UNIXタイムスタンプ(ミリ秒): {datenum}\n")