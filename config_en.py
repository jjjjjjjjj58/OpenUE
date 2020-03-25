import os 
class config():
    input_dir = ''
    max_len = '128'
    pretrain_model_dir = ''
    home_dir = os.getcwd() + '/' 
    data_dir = home_dir + 'raw_data/event_cn/'
    tf_serving_addr = '127.0.0.1:8501'
    bert_vocab_dir = home_dir + 'pretrained_model/bert/vocab.txt'
    bert_config_dir =home_dir + 'pretrained_model/bert/bert_config.json'
    #bert_vocab_dir = home_dir + 'pretrained_model/chinese_sbert_WZN_ml-128_L-4_H-256_A-4_D-large_K-2_a-ann/vocab.txt'
    #bert_config_dir =home_dir + 'pretrained_model/chinese_sbert_WZN_ml-128_L-4_H-256_A-4_D-large_K-2_a-ann/bert_config.json'

    class_model_dir = 'output/predicate_classification_model/epochs6/model.ckpt-6000'
    seq_model_dir = 'output/sequnce_labeling_model/epochs9/model.ckpt-85304'
    middle_out_dir = './output/predicate_infer_out'
    out_dir = './output/sequnce_infer_out/epochs9/ckpt22000'
    token_label = ["[Padding]", "[category]", "[##WordPiece]", "[CLS]", "[SEP]", "B-SUB", "I-SUB", "B-OBJ", "I-OBJ", "O"]  #id 0 --> [Paddding]
    #token_label = ["[Padding]", "[category]", "[##WordPiece]", "[CLS]", "[SEP]", "B-location", "I-location", "B-time", "I-time", "B-object", "I-object","B-participant", "I-participant","B-denoter", "I-denoter","O"]  #id 0 --> [Paddding]
    #class_label = ['accident', 'fire', 'terrorism', 'earthquake', 'poison']

    #class_label =  ['丈夫', '上映时间', '专业代码', '主持人', '主演', '主角', '人口数量', '作曲', '作者', '作词', '修业年限', '出品公司', '出版社', '出生地', '出生日期','创始人', '制片人', '占地面积', '号', '嘉宾', '国籍', '妻子', '字', '官方语言', '导演', '总部地点', '成立日期', '所在城市', '所属专辑', '改编自', '朝代', '歌手', '母亲', '毕业院校', '民族', '气候', '注册资本', '海拔', '父亲', '目', '祖籍', '简称', '编剧', '董事长', '身高', '连载网站','邮政编码', '面积', '首都']
    class_label = ['P20', 'P397', 'P376', 'P31', 'P0', 'P641', 'P737', 'P161', 'P413', 'P47', 'P530', 'P131', 'P159', 'P176', 'P179', 'P279', 'P400', 'P155', 'P452', 'P36', 'P276', 'P361', 'P17', 'P495', 'P449', 'P54', 'P607', 'P403', 'P1344', 'P27', 'P19', 'P118', 'P108', 'P264', 'P460', 'P501', 'P69', 'P106', 'P735', 'P706', 'P138', 'P463', 'P241', 'P57', 'P1365', 'P144', 'P170', 'P577', 'P2416', 'P1336', 'P40', 'P178', 'P175', 'P190', 'P22', 'P197', 'P126', 'P50', 'P664', 'P571', 'P26', 'P136', 'P102', 'P1001', 'P570', 'P800', 'P1027', 'P569', 'P674', 'P1408', 'P1072', 'P1038', 'P9', 'P86', 'P39', 'P466', 'P150', 'P37', 'P121', 'P112', 'P123', 'P1383', 'P272', 'P30', 'P1080', 'P59', 'P937', 'P186', 'P306', 'P355', 'P166', 'P425', 'P7', 'P1412', 'P263', 'P360', 'P127', 'P412', 'P53', 'P1142', 'P101', 'P81', 'P740', 'P1589', 'P35', 'P58', 'P194', 'P629', 'P140', 'P991', 'P1435', 'P61', 'P206', 'P611', 'P275', 'P1346', 'P97', 'P551', 'P734', 'P461', 'P2079', 'P921', 'P162', 'P135', 'P157', 'P371', 'P172', 'P1269', 'P407', 'P1303', 'P2578', 'P277', 'P287', 'P541', 'P1196', 'P115', 'P1302', 'P1191', 'P163', 'P559', 'P205', 'P1582', 'P509', 'P25', 'P177', 'P725', 'P119', 'P828', 'P647', 'P553', 'P708', 'P1809', 'P450', 'P765', 'P84', 'P2389', 'P410', 'P111', 'P676', 'P575', 'P1532', 'P840', 'P149', 'P366', 'P1040', 'P1312', 'P103', 'P1995', 'P364', 'P1049', 'P793', 'P408', 'P941', 'P807', 'P209', 'P16', 'P915', 'P802', 'P6', 'P1313', 'P1889', 'P1891', 'P184', 'P451', 'P1431', 'P1056', 'P669', 'P726', 'P750', 'P87', 'P1192', 'P945', 'P122', 'P180', 'P415', 'P113', 'P2348', 'P780', 'P729', 'P832', 'P1411', 'P748', 'P411', 'P1962', 'P1619', 'P2541', 'P282', 'P1885', 'P141', 'P406', 'P85', 'P286', 'P880', 'P169', 'P2596', 'P469', 'P1071', 'P610', 'P2098', 'P1050', 'P522', 'P619', 'P609', 'P183', 'P972', 'P689', 'P2512', 'P1535', 'P91', 'P703', 'P98', 'P2546', 'P1571', 'P38', 'P344', 'P291', 'P462', 'P1308', 'P1434', 'P92', 'P1990', 'P1064', 'P1654', 'P931', 'P1811', 'P66', 'P289', 'P1557', 'P414', 'P826', 'P1327', 'P1317', 'P2289', 'P1399', 'P658', 'P523', 'P516', 'P767', 'P2152', 'P1181', 'P437', 'P195', 'P199', 'P208', 'P1622', 'P417', 'P885', 'P1731', 'P1165', 'P770', 'P110', 'P1068', 'P2505', 'P517', 'P684', 'P457', 'P1074', 'P512', 'P237', 'P825', 'P1851', 'P2632', 'P1462', 'P2341', 'P1433', 'P1416', 'P730', 'P547', 'P201', 'P655', 'P134', 'P1479', 'P1455', 'P88', 'P1478', 'P831', 'P562', 'P870', 'P189', 'P533', 'P1531', 'P375', 'P927', 'P2155', 'P421', 'P200', 'P790', 'P1268', 'P1389', 'P769', 'P822', 'P196', 'P618', 'P114', 'P620', 'P1574', 'P504', 'P21', 'P1875', 'P2633', 'P467', 'P1906', 'P500', 'P1363', 'P2184', 'P2286', 'P1018', 'P1249', 'P2670', 'P688', 'P1158', 'P1057', 'P2293', 'P1552', 'P1382', 'P788', 'P612', 'P768', 'P485', 'P913', 'P567', 'P1429', 'P681', 'P1420', 'P427', 'P1322', 'P1414', 'P868', 'P399', 'P1081', 'P1547', 'P1560']
    schema = {
    '父亲': [('人物', '人物')],
    '妻子': [('人物', '人物')],
    '母亲': [('人物', '人物')],
    '丈夫': [('人物', '人物')],
    '祖籍': [('地点', '人物')],
    '总部地点': [('地点', '企业')],
    '出生地': [('地点', '人物')],
    '目': [('目', '生物')],
    '面积': [('Number', '行政区')],
    '简称': [('Text', '机构')],
    '上映时间': [('Date', '影视作品')],
    '所属专辑': [('音乐专辑', '歌曲')],
    '注册资本': [('Number', '企业')],
    '首都': [('城市', '国家')],
    '导演': [('人物', '影视作品')],
    '字': [('Text', '历史人物')],
    '身高': [('Number', '人物')],
    '出品公司': [('企业', '影视作品')],
    '修业年限': [('Number', '学科专业')],
    '出生日期': [('Date', '人物')],
    '制片人': [('人物', '影视作品')],
    '编剧': [('人物', '影视作品')],
    '国籍': [('国家', '人物')],
    '海拔': [('Number', '地点')],
    '连载网站': [('网站', '网络小说')],
    '朝代': [('Text', '历史人物')],
    '民族': [('Text', '人物')],
    '号': [('Text', '历史人物')],
    '出版社': [('出版社', '书籍')],
    '主持人': [('人物', '电视综艺')],
    '专业代码': [('Text', '学科专业')],
    '歌手': [('人物', '歌曲')],
    '作词': [('人物', '歌曲')],
    '主角': [('人物', '网络小说')],
    '董事长': [('人物', '企业')],
    '成立日期': [('Date', '机构'), ('Date', '企业')],
    '毕业院校': [('学校', '人物')],
    '占地面积': [('Number', '机构')],
    '官方语言': [('语言', '国家')],
    '邮政编码': [('Text', '行政区')],
    '人口数量': [('Number', '行政区')],
    '所在城市': [('城市', '景点')],
    '作者': [('人物', '图书作品')],
    '作曲': [('人物', '歌曲')],
    '气候': [('气候', '行政区')],
    '嘉宾': [('人物', '电视综艺')],
    '主演': [('人物', '影视作品')],
    '改编自': [('作品', '影视作品')],
    '创始人': [('人物', '企业')]}