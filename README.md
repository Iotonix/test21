# Lingo
The Language Service is used for internationalization of all products (Mobile and Web). 
The StringKeys and ID's are mapped to translations.


## Load configuartions 
Download: http://vo2.tech/Z1ivMYXLt8D as xlsx file 
Create the Platforms WEB, MOBILE, KYC2 in platforms via the django admin as following

| Name   | Start Row | default Col | Key Col | Translation Start Column | Regex                              |
| ------ | --------- | ----------- | ------- | ------------------------ | ---------------------------------- |
| WEB    | 3         | 5           | 3       | 7                        | ^\.([a-zA-Z]{2}\|[a-zA-Z]{3})_(.*) |
| MOBILE | 3         | 2           | 1       | 3                        | ^\.([a-zA-Z]{2}\|[a-zA-Z]{3})_(.*) |
| KYC2   | 3         | 2           | 1       | 3                        | ^\.([a-zA-Z]{2}\|[a-zA-Z]{3})_(.*) |


Create the Language master records as:
|name_en|name|locale|
|--- |--- |--- |
|English (United States)|American English|en_US|
|German (Germany)|Deutsch (Deutschland)|de_DE|
|French (France)|français (France)|fr_FR|
|Arabic (U.A.E.)|Arabic (U.A.E.)|ar_AE|
|Filipino (Philippines)|Filipino (Pilipinas)|fil_PH|
|Khmer (Cambodia)|ខ្មែរ (កម្ពុជា)|km_kh|
|Russian (Russia)|русский (Россия)|ru_RU|
|Thai (Thailand)|ไทย (ไทย)|th_TH|
|Chinese (Simplified, China)|中文（简体，中国）|zh_Hans_CN|
|Japanese (Japan)|日本語 (日本)|ja_JP|
|Korean (South Korea)|한국어(대한민국)|ko_KR|
|Spanish (Spain)|español (España)|es_ES|



## Angular approach ##

Ralf Hundertmark, [12.09.19 08:57]
location: ~/assets/strings.json
[
    { key: 'DASHBOARD.KYC_LEVEL_1': text: 'KYC Level 1' },
    { key: 'DASHBOARD.KYC_LEVEL_2': text: 'KYC Level 2' },
    { key: 'DASHBOARD.KYC_LEVEL_3': text: 'KYC Level 3' },
    { key: 'LOGIN.USER_NAME': text: 'Username' },
]

<p>{{ get_translation(DASHBOARD.KYC_LEVEL_1) }}</p>

get_translation(key: string) => Service // read localStorage or redux service  = returns string
get_translations(language: string) => call REST language service = returns JSON



## What is this repository for? ###

* App developers 
* Version 0.0.1


## How do I get set up? ###

* git clone ths repo
