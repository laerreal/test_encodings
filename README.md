A Test suite for `str` <=> `bytes` codecs of Python.
I.e., for `encoding` argument values of `bytes.decode` or `str.encode`.

## test_encodings.py

* finds out available codecs
* finds out "universal" codecs (those who can decode all byte values [0;255])
* measures time of decoding, encoding and total

## `main.py`

* executes test for all available interpreters

### Example

```bash
$ ./main.py
Interpreter: /usr/bin/python
Available interpreters: /usr/bin/python2.7, /usr/bin/python3.5
Launching /usr/bin/python2.7 ./test_encodings.py
Python version: 2.7.12 (default, Nov 12 2018, 14:36:49) 
[GCC 5.4.0 20160609]
Looking for codecs in /usr/lib/python2.7/encodings
Possible encodings: cp424, utf_16_le, utf_32_le, euc_jp, cp863, iso8859_9, shift_jis_2004, idna, cp1140, utf_16, iso8859_16, cp1258, cp1255, iso8859_4, zlib_codec, cp866, big5hkscs, big5, base64_codec, iso8859_14, koi8_u, mbcs, cp1253, unicode_escape, mac_greek, cp855, undefined, cp857, cp932, iso2022_jp_2004, cp860, iso8859_1, cp1254, iso2022_kr, raw_unicode_escape, utf_8_sig, mac_latin2, cp852, mac_iceland, iso2022_jp, iso2022_jp_2, hex_codec, hp_roman8, latin_1, iso8859_2, koi8_r, cp775, quopri_codec, cp865, punycode, cp1256, iso8859_7, gbk, johab, hz, mac_roman, iso2022_jp_3, unicode_internal, cp850, mac_cyrillic, euc_kr, charmap, ptcp154, cp437, cp949, cp858, cp1026, mac_turkish, cp950, utf_32_be, utf_32, shift_jis, cp720, __init__, iso8859_6, cp500, utf_16_be, cp856, gb18030, cp862, cp1006, utf_7, cp861, iso8859_13, gb2312, cp864, tis_620, cp1250, iso8859_10, string_escape, iso8859_5, uu_codec, iso8859_3, rot_13, shift_jisx0213, cp037, iso2022_jp_1, mac_croatian, euc_jis_2004, cp1252, mac_centeuro, ascii, mac_farsi, palmos, cp1257, aliases, iso8859_8, cp874, mac_romanian, euc_jisx0213, iso8859_15, cp1251, mac_arabic, utf_8, iso8859_11, cp869, cp875, cp737, bz2_codec, iso2022_jp_ext
Encodings: cp424, utf_16_le, utf_32_le, euc_jp, cp863, iso8859_9, shift_jis_2004, idna, cp1140, utf_16, iso8859_16, cp1258, cp1255, iso8859_4, zlib_codec, cp866, big5hkscs, big5, base64_codec, iso8859_14, koi8_u, cp1253, unicode_escape, mac_greek, cp855, undefined, cp857, cp932, iso2022_jp_2004, cp860, iso8859_1, cp1254, iso2022_kr, raw_unicode_escape, utf_8_sig, mac_latin2, cp852, mac_iceland, iso2022_jp, iso2022_jp_2, hex_codec, hp_roman8, latin_1, iso8859_2, koi8_r, cp775, quopri_codec, cp865, punycode, cp1256, iso8859_7, gbk, johab, hz, mac_roman, iso2022_jp_3, unicode_internal, cp850, mac_cyrillic, euc_kr, charmap, ptcp154, cp437, cp949, cp858, cp1026, mac_turkish, cp950, utf_32_be, utf_32, shift_jis, cp720, iso8859_6, cp500, utf_16_be, cp856, gb18030, cp862, cp1006, utf_7, cp861, iso8859_13, gb2312, cp864, tis_620, cp1250, iso8859_10, string_escape, iso8859_5, uu_codec, iso8859_3, rot_13, shift_jisx0213, cp037, iso2022_jp_1, mac_croatian, euc_jis_2004, cp1252, mac_centeuro, ascii, mac_farsi, palmos, cp1257, iso8859_8, cp874, mac_romanian, euc_jisx0213, iso8859_15, cp1251, mac_arabic, utf_8, iso8859_11, cp869, cp875, cp737, bz2_codec, iso2022_jp_ext
Universal encodings: cp863, iso8859_9, cp1140, iso8859_16, iso8859_4, cp866, iso8859_14, koi8_u, mac_greek, cp855, cp860, iso8859_1, raw_unicode_escape, mac_latin2, cp852, mac_iceland, latin_1, iso8859_2, koi8_r, cp775, cp865, cp1256, mac_roman, cp850, mac_cyrillic, charmap, ptcp154, cp437, cp858, cp1026, mac_turkish, cp720, cp500, cp862, cp861, iso8859_13, iso8859_10, iso8859_5, rot_13, cp037, mac_croatian, mac_centeuro, palmos, mac_romanian, iso8859_15, cp737
Test data length 8388608B
measuring cp863
measuring iso8859_9
measuring cp1140
measuring iso8859_16
measuring iso8859_4
measuring cp866
measuring iso8859_14
measuring koi8_u
measuring mac_greek
measuring cp855
measuring cp860
measuring iso8859_1
measuring raw_unicode_escape
measuring mac_latin2
measuring cp852
measuring mac_iceland
measuring latin_1
measuring iso8859_2
measuring koi8_r
measuring cp775
measuring cp865
measuring cp1256
measuring mac_roman
measuring cp850
measuring mac_cyrillic
measuring charmap
measuring ptcp154
measuring cp437
measuring cp858
measuring cp1026
measuring mac_turkish
measuring cp720
measuring cp500
measuring cp862
measuring cp861
measuring iso8859_13
measuring iso8859_10
measuring iso8859_5
measuring rot_13
measuring cp037
measuring mac_croatian
measuring mac_centeuro
measuring palmos
measuring mac_romanian
measuring iso8859_15
measuring cp737
Codec              ; Decoding time    ; Encoding time    ; Total
iso8859_1          ; 0.00999307632446 ; 0.00446605682373 ; 0.0144591331482
charmap            ; 0.010330915451   ; 0.00444793701172 ; 0.0147788524628
latin_1            ; 0.0102500915527  ; 0.00456786155701 ; 0.0148179531097
raw_unicode_escape ; 0.0268270969391  ; 0.011656999588   ; 0.0384840965271
iso8859_4          ; 0.0233240127563  ; 0.0256750583649  ; 0.0489990711212
mac_croatian       ; 0.0233800411224  ; 0.0256590843201  ; 0.0490391254425
mac_roman          ; 0.0234429836273  ; 0.0257091522217  ; 0.049152135849
koi8_r             ; 0.0235052108765  ; 0.0257208347321  ; 0.0492260456085
iso8859_10         ; 0.0235500335693  ; 0.0257461071014  ; 0.0492961406708
cp037              ; 0.0234069824219  ; 0.0259599685669  ; 0.0493669509888
mac_cyrillic       ; 0.0233521461487  ; 0.0260708332062  ; 0.0494229793549
mac_romanian       ; 0.0234699249268  ; 0.0259919166565  ; 0.0494618415833
koi8_u             ; 0.0236501693726  ; 0.0259540081024  ; 0.049604177475
iso8859_16         ; 0.0234518051147  ; 0.0262241363525  ; 0.0496759414673
iso8859_13         ; 0.0236368179321  ; 0.0260419845581  ; 0.0496788024902
cp1140             ; 0.0235800743103  ; 0.0262048244476  ; 0.0497848987579
iso8859_14         ; 0.0232989788055  ; 0.0264859199524  ; 0.0497848987579
iso8859_15         ; 0.0239369869232  ; 0.0259351730347  ; 0.0498721599579
mac_centeuro       ; 0.0235698223114  ; 0.0263919830322  ; 0.0499618053436
iso8859_2          ; 0.0237011909485  ; 0.026261806488   ; 0.0499629974365
mac_greek          ; 0.0237770080566  ; 0.0262889862061  ; 0.0500659942627
iso8859_5          ; 0.0238449573517  ; 0.0263230800629  ; 0.0501680374146
cp1256             ; 0.0236279964447  ; 0.0265529155731  ; 0.0501809120178
cp500              ; 0.024032831192   ; 0.0263290405273  ; 0.0503618717194
mac_turkish        ; 0.0239510536194  ; 0.0264461040497  ; 0.0503971576691
mac_iceland        ; 0.02397108078    ; 0.0264420509338  ; 0.0504131317139
cp720              ; 0.0243539810181  ; 0.0265741348267  ; 0.0509281158447
cp1026             ; 0.0243401527405  ; 0.0270800590515  ; 0.051420211792
iso8859_9          ; 0.0235528945923  ; 0.0282640457153  ; 0.0518169403076
cp850              ; 0.0235888957977  ; 0.124856948853   ; 0.14844584465
cp858              ; 0.0235538482666  ; 0.125432014465   ; 0.148985862732
cp860              ; 0.023558139801   ; 0.139779806137   ; 0.163337945938
cp865              ; 0.0232679843903  ; 0.14112496376    ; 0.164392948151
cp437              ; 0.0236420631409  ; 0.140780925751   ; 0.164422988892
cp861              ; 0.0245242118835  ; 0.142044782639   ; 0.166568994522
cp775              ; 0.0233669281006  ; 0.148489952087   ; 0.171856880188
cp737              ; 0.0233190059662  ; 0.15801692009    ; 0.181335926056
cp862              ; 0.0238871574402  ; 0.161686897278   ; 0.185574054718
cp852              ; 0.0238947868347  ; 0.163340091705   ; 0.18723487854
cp866              ; 0.0234010219574  ; 0.16801905632    ; 0.191420078278
cp855              ; 0.0234417915344  ; 0.175350189209   ; 0.198791980743
cp863              ; 0.0381789207458  ; 0.180813074112   ; 0.218991994858
rot_13             ; 0.119679927826   ; 0.118031978607   ; 0.237711906433
palmos             ; 0.118813037872   ; 0.124657154083   ; 0.243470191956
mac_latin2         ; 0.119580030441   ; 0.157041072845   ; 0.276621103287
ptcp154            ; 0.118884086609   ; 0.169498920441   ; 0.28838300705
Launching /usr/bin/python3.5 ./test_encodings.py
Python version: 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609]
Looking for codecs in /usr/lib/python3.5/encodings
Possible encodings: cp424, utf_16_le, utf_32_le, euc_jp, cp863, iso8859_9, cp1125, shift_jis_2004, idna, cp1140, utf_16, iso8859_16, cp1258, cp65001, cp1255, iso8859_4, zlib_codec, cp866, big5hkscs, big5, base64_codec, iso8859_14, koi8_u, mbcs, cp1253, unicode_escape, mac_greek, cp855, undefined, cp857, kz1048, cp932, iso2022_jp_2004, cp860, iso8859_1, cp1254, iso2022_kr, raw_unicode_escape, utf_8_sig, mac_latin2, cp852, mac_iceland, iso2022_jp, iso2022_jp_2, hex_codec, hp_roman8, latin_1, iso8859_2, koi8_r, cp775, quopri_codec, cp865, punycode, cp1256, iso8859_7, gbk, johab, hz, mac_roman, iso2022_jp_3, unicode_internal, cp850, mac_cyrillic, euc_kr, charmap, ptcp154, cp437, cp949, cp858, cp1026, mac_turkish, cp950, utf_32_be, utf_32, shift_jis, cp720, __init__, cp273, iso8859_6, cp500, utf_16_be, cp856, gb18030, cp862, cp1006, utf_7, cp861, iso8859_13, gb2312, cp864, tis_620, cp1250, iso8859_10, iso8859_5, uu_codec, iso8859_3, rot_13, shift_jisx0213, cp037, iso2022_jp_1, mac_croatian, euc_jis_2004, cp1252, mac_centeuro, ascii, mac_farsi, palmos, cp1257, aliases, iso8859_8, koi8_t, cp874, mac_romanian, euc_jisx0213, iso8859_15, cp1251, mac_arabic, utf_8, iso8859_11, cp869, cp875, cp737, bz2_codec, iso2022_jp_ext
Encodings: cp424, utf_16_le, utf_32_le, euc_jp, cp863, iso8859_9, cp1125, shift_jis_2004, idna, cp1140, utf_16, iso8859_16, cp1258, cp1255, iso8859_4, zlib_codec, cp866, big5hkscs, big5, base64_codec, iso8859_14, koi8_u, cp1253, unicode_escape, mac_greek, cp855, undefined, cp857, kz1048, cp932, iso2022_jp_2004, cp860, iso8859_1, cp1254, iso2022_kr, raw_unicode_escape, utf_8_sig, mac_latin2, cp852, mac_iceland, iso2022_jp, iso2022_jp_2, hex_codec, hp_roman8, latin_1, iso8859_2, koi8_r, cp775, quopri_codec, cp865, punycode, cp1256, iso8859_7, gbk, johab, hz, mac_roman, iso2022_jp_3, unicode_internal, cp850, mac_cyrillic, euc_kr, charmap, ptcp154, cp437, cp949, cp858, cp1026, mac_turkish, cp950, utf_32_be, utf_32, shift_jis, cp720, cp273, iso8859_6, cp500, utf_16_be, cp856, gb18030, cp862, cp1006, utf_7, cp861, iso8859_13, gb2312, cp864, tis_620, cp1250, iso8859_10, iso8859_5, uu_codec, iso8859_3, rot_13, shift_jisx0213, cp037, iso2022_jp_1, mac_croatian, euc_jis_2004, cp1252, mac_centeuro, ascii, mac_farsi, palmos, cp1257, iso8859_8, koi8_t, cp874, mac_romanian, euc_jisx0213, iso8859_15, cp1251, mac_arabic, utf_8, iso8859_11, cp869, cp875, cp737, bz2_codec, iso2022_jp_ext
Universal encodings: cp863, iso8859_9, cp1125, cp1140, iso8859_16, iso8859_4, cp866, iso8859_14, koi8_u, mac_greek, cp855, cp860, iso8859_1, raw_unicode_escape, mac_latin2, cp852, mac_iceland, latin_1, iso8859_2, koi8_r, cp775, cp865, cp1256, mac_roman, cp850, mac_cyrillic, charmap, ptcp154, cp437, cp858, cp1026, mac_turkish, cp720, cp273, cp500, cp862, cp861, iso8859_13, iso8859_10, iso8859_5, cp037, mac_croatian, mac_centeuro, palmos, mac_romanian, iso8859_15, cp737
Test data length 8388608B
measuring cp863
measuring iso8859_9
measuring cp1125
measuring cp1140
measuring iso8859_16
measuring iso8859_4
measuring cp866
measuring iso8859_14
measuring koi8_u
measuring mac_greek
measuring cp855
measuring cp860
measuring iso8859_1
measuring raw_unicode_escape
measuring mac_latin2
measuring cp852
measuring mac_iceland
measuring latin_1
measuring iso8859_2
measuring koi8_r
measuring cp775
measuring cp865
measuring cp1256
measuring mac_roman
measuring cp850
measuring mac_cyrillic
measuring charmap
measuring ptcp154
measuring cp437
measuring cp858
measuring cp1026
measuring mac_turkish
measuring cp720
measuring cp273
measuring cp500
measuring cp862
measuring cp861
measuring iso8859_13
measuring iso8859_10
measuring iso8859_5
measuring cp037
measuring mac_croatian
measuring mac_centeuro
measuring palmos
measuring mac_romanian
measuring iso8859_15
measuring cp737
Codec              ; Decoding time         ; Encoding time        ; Total
iso8859_1          ; 0.0031402111053466797 ; 0.002582073211669922 ; 0.0057222843170166016
latin_1            ; 0.003465414047241211  ; 0.002523660659790039 ; 0.00598907470703125
charmap            ; 0.0031697750091552734 ; 0.006281614303588867 ; 0.00945138931274414
raw_unicode_escape ; 0.01974344253540039   ; 0.004955291748046875 ; 0.024698734283447266
cp037              ; 0.017766952514648438  ; 0.021737098693847656 ; 0.039504051208496094
cp500              ; 0.017584562301635742  ; 0.02192068099975586  ; 0.0395052433013916
cp720              ; 0.014564037322998047  ; 0.027846574783325195 ; 0.04241061210632324
mac_greek          ; 0.014556646347045898  ; 0.028109073638916016 ; 0.042665719985961914
iso8859_5          ; 0.01433420181274414   ; 0.028377294540405273 ; 0.042711496353149414
iso8859_13         ; 0.014500617980957031  ; 0.028244972229003906 ; 0.04274559020996094
koi8_u             ; 0.014530658721923828  ; 0.028217792510986328 ; 0.042748451232910156
mac_iceland        ; 0.014639616012573242  ; 0.028307437896728516 ; 0.04294705390930176
mac_cyrillic       ; 0.014651060104370117  ; 0.028325557708740234 ; 0.04297661781311035
iso8859_10         ; 0.014822721481323242  ; 0.028208494186401367 ; 0.04303121566772461
cp273              ; 0.014753580093383789  ; 0.028298377990722656 ; 0.043051958084106445
iso8859_4          ; 0.01518559455871582   ; 0.02808547019958496  ; 0.04327106475830078
iso8859_14         ; 0.014824867248535156  ; 0.02851581573486328  ; 0.04334068298339844
iso8859_15         ; 0.015943050384521484  ; 0.028177738189697266 ; 0.04412078857421875
cp1256             ; 0.01629638671875      ; 0.028479576110839844 ; 0.044775962829589844
koi8_r             ; 0.016965389251708984  ; 0.027846097946166992 ; 0.04481148719787598
iso8859_16         ; 0.016292810440063477  ; 0.029135942459106445 ; 0.04542875289916992
mac_centeuro       ; 0.017757177352905273  ; 0.028137922286987305 ; 0.04589509963989258
cp1026             ; 0.017639636993408203  ; 0.028418779373168945 ; 0.04605841636657715
palmos             ; 0.0179135799407959    ; 0.028165102005004883 ; 0.04607868194580078
mac_roman          ; 0.017995834350585938  ; 0.028146982192993164 ; 0.0461428165435791
ptcp154            ; 0.018311500549316406  ; 0.028018951416015625 ; 0.04633045196533203
iso8859_2          ; 0.01824045181274414   ; 0.028211116790771484 ; 0.046451568603515625
mac_croatian       ; 0.018233060836791992  ; 0.02828812599182129  ; 0.04652118682861328
mac_turkish        ; 0.017754316329956055  ; 0.028916358947753906 ; 0.04667067527770996
mac_latin2         ; 0.01827836036682129   ; 0.028680086135864258 ; 0.04695844650268555
cp1140             ; 0.01847386360168457   ; 0.0284881591796875   ; 0.04696202278137207
mac_romanian       ; 0.01842021942138672   ; 0.02914118766784668  ; 0.0475614070892334
iso8859_9          ; 0.019534587860107422  ; 0.03060007095336914  ; 0.05013465881347656
cp858              ; 0.018273115158081055  ; 0.1986839771270752   ; 0.21695709228515625
cp850              ; 0.0165407657623291    ; 0.2005910873413086   ; 0.2171318531036377
cp860              ; 0.014807462692260742  ; 0.23314476013183594  ; 0.24795222282409668
cp861              ; 0.017941713333129883  ; 0.23238039016723633  ; 0.2503221035003662
cp437              ; 0.01808452606201172   ; 0.23465609550476074  ; 0.25274062156677246
cp865              ; 0.01819920539855957   ; 0.23481225967407227  ; 0.25301146507263184
cp863              ; 0.01908707618713379   ; 0.2463996410369873   ; 0.2654867172241211
cp852              ; 0.017914772033691406  ; 0.25195932388305664  ; 0.26987409591674805
cp862              ; 0.017918109893798828  ; 0.25656557083129883  ; 0.27448368072509766
cp775              ; 0.014839649200439453  ; 0.2624368667602539   ; 0.27727651596069336
cp737              ; 0.014657735824584961  ; 0.2683863639831543   ; 0.28304409980773926
cp866              ; 0.015011072158813477  ; 0.28215909004211426  ; 0.29717016220092773
cp1125             ; 0.018945693969726562  ; 0.28275060653686523  ; 0.3016963005065918
cp855              ; 0.014958858489990234  ; 0.2900502681732178   ; 0.305009126663208
```
