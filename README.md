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

```{shell}
python getData.py [存放檔案路徑]
```

執行下面這段，講資料轉成csv
```{shell}
python transformData.py [存放檔案路徑] [Currency_Code(USD)]
```

## [匯率資料](https://github.com/ntuaha/Path_Simplification/blob/dev/data/USD.csv)

1. 時間 2006/01/01 - 2014/09/27
2. 時間間距 從1970/01/01到資料日期的**天數**
3. USD.csv  美金對台幣的匯率



