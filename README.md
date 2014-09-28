Path_Simplification
===================

Simplify your path, curve, or curve under some specific criteria.

## Data

- 從 [https://www.cathaybk.com.tw/cathaybk/personal_info14_excel.asp](https://www.cathaybk.com.tw/cathaybk/personal_info14_excel.asp)利用POST傳送  

	- SelCur=USD3%AC%FC%A4%B8&R1=2
	- BDate=2014%2F06%2F27
	- EDate=2014%2F09%2F27

Example Code
```{shell}
curl -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31" --data "SelCur=USD3%AC%FC%A4%B8&R1=2&BDate=2014%2F01%2F01&EDate=2015%2F12%2F31" -o ../data/20140101_20151231.xls https://www.cathaybk.com.tw/cathaybk/personal_info14_excel.asp
```

可以直接執行,會自動下載從2006到現在的檔案

```
python getData.py [存放檔案路徑]
```

