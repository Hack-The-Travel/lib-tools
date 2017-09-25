# coding: utf-8
import sys
if sys.version_info[0] < 3:
    from io import open
import simplejson
from lxml import etree


citizenship_rus = '''
<select class="_1-1-23_djFYx" placeholder="Гражданство" name="passengers[0].passCountry" format="function a(e){return e}"><option value="AU">Австралия</option><option value="AT">Австрия</option><option value="AZ">Азербайджан</option><option value="AL">Албания</option><option value="DZ">Алжир</option><option value="AO">Ангола</option><option value="AR">Аргентина</option><option value="AM">Армения</option><option value="AF">Афганистан</option><option value="BD">Бангладеш</option><option value="BH">Бахрейн</option><option value="BY">Беларусь</option><option value="BE">Бельгия</option><option value="BG">Болгария</option><option value="BO">Боливия</option><option value="BA">Босния и Герцеговина</option><option value="BW">Ботсвана</option><option value="BR">Бразилия</option><option value="BF">Буркина-Фасо</option><option value="GB">Великобритания</option><option value="HU">Венгрия</option><option value="VE">Венесуэла</option><option value="VN">Вьетнам</option><option value="HT">Гаити</option><option value="GY">Гайана</option><option value="GM">Гамбия</option><option value="GH">Гана</option><option value="GT">Гватемала</option><option value="DE">Германия</option><option value="HN">Гондурас</option><option value="HK">Гонконг</option><option value="GR">Греция</option><option value="GE">Грузия</option><option value="DK">Дания</option><option value="DO">Доминиканская Республика</option><option value="EG">Египет</option><option value="ZM">Замбия</option><option value="ZW">Зимбабве</option><option value="zw">Зимбабве</option><option value="IL">Израиль</option><option value="IN">Индия</option><option value="ID">Индонезия</option><option value="JO">Иордания</option><option value="IQ">Ирак</option><option value="IR">Иран</option><option value="IE">Ирландия</option><option value="IS">Исландия</option><option value="ES">Испания</option><option value="IT">Италия</option><option value="YE">Йемен</option><option value="KZ">Казахстан</option><option value="KH">Камбоджа</option><option value="CM">Камерун</option><option value="CA">Канада</option><option value="QA">Катар</option><option value="KE">Кения</option><option value="CY">Кипр</option><option value="KG">Киргизия</option><option value="CN">Китай</option><option value="CO">Колумбия</option><option value="CG">Конго Республика</option><option value="KP">Корея (Северная), КНДР</option><option value="KR">Корея (Южная)</option><option value="CR">Коста-Рика</option><option value="CI">Кот-д'Ивуар</option><option value="CU">Куба</option><option value="KW">Кувейт</option><option value="LV">Латвия</option><option value="LB">Ливан</option><option value="LY">Ливия</option><option value="LT">Литва</option><option value="LU">Люксембург</option><option value="MU">Маврикий</option><option value="MG">Мадагаскар</option><option value="MO">Макао</option><option value="MK">Македония</option><option value="MY">Малайзия</option><option value="ML">Мали</option><option value="MT">Мальта</option><option value="MA">Марокко</option><option value="MX">Мексика</option><option value="MZ">Мозамбик</option><option value="MD">Молдавия</option><option value="MC">Монако</option><option value="MN">Монголия</option><option value="NA">Намибия</option><option value="NP">Непал</option><option value="NG">Нигерия</option><option value="NL">Нидерланды</option><option value="NI">Никарагуа</option><option value="NZ">Новая Зеландия</option><option value="NO">Норвегия</option><option value="AE">ОАЭ</option><option value="OM">Оман</option><option value="PK">Пакистан</option><option value="PS">Палестина</option><option value="PA">Панама</option><option value="PY">Парагвай</option><option value="PE">Перу</option><option value="PL">Польша</option><option value="PT">Португалия</option><option value="PR">Пуэрто-Рико</option><option value="Гана">Республика Гана</option><option value="RU">Россия</option><option value="RW">Руанда</option><option value="RO">Румыния</option><option value="SA">Саудовская Аравия</option><option value="SN">Сенегал</option><option value="VC">Сент-Винсент и Гренадины</option><option value="RS">Сербия</option><option value="SG">Сингапур</option><option value="SY">Сирия</option><option value="SK">Словакия</option><option value="SI">Словения</option><option value="US">США</option><option value="SL">Сьерра-Леоне</option><option value="TJ">Таджикистан</option><option value="TH">Таиланд</option><option value="TW">Тайвань</option><option value="TZ">Танзания</option><option value="TG">Того</option><option value="TT">Тринидад и Тобаго</option><option value="TN">Тунис</option><option value="TM">Туркменистан</option><option value="TR">Турция</option><option value="UG">Уганда</option><option value="UZ">Узбекистан</option><option value="UA">Украина</option><option value="UY">Уругвай</option><option value="PH">Филиппины</option><option value="FI">Финляндия</option><option value="FR">Франция</option><option value="HR">Хорватия</option><option value="TD">Чад</option><option value="ME">Черногория</option><option value="CZ">Чехия</option><option value="CL">Чили</option><option value="CH">Швейцария</option><option value="SE">Швеция</option><option value="LK">Шри-Ланка</option><option value="EC">Эквадор</option><option value="GQ">Экваториальная Гвинея</option><option value="SV">Эль-Сальвадор</option><option value="EE">Эстония</option><option value="ET">Эфиопия</option><option value="ZA">ЮАР</option><option value="JM">Ямайка</option><option value="JP">Япония</option></select>
'''
citizenship_eng = '''
<select class="_1-1-23_djFYx" placeholder="Citizenship" name="passengers[0].passCountry" format="function a(e){return e}"><option value="AF">Afghanistan</option><option value="AL">Albania</option><option value="DZ">Algeria</option><option value="AO">Angola</option><option value="AR">Argen</option><option value="AM">Armenia</option><option value="AU">Australia</option><option value="AT">Austria</option><option value="AZ">Azerbaijan</option><option value="BH">Bahrain</option><option value="BD">Bangladesh</option><option value="BY">Belarus</option><option value="BE">Belgium</option><option value="BO">Bolivia</option><option value="BA">Bosnia Herzegovina</option><option value="BW">Botswana</option><option value="BR">Brazil</option><option value="BG">Bulgaria</option><option value="BF">Burkina Faso</option><option value="KH">Cambodia</option><option value="CM">Cameroon, United Republic Of</option><option value="CA">Canada</option><option value="TD">Chad</option><option value="CL">Chile</option><option value="CN">China</option><option value="CO">Colombia</option><option value="CG">Congo Republic</option><option value="CR">Costa Rica</option><option value="CI">Cote d'Ivoire</option><option value="HR">Croatia</option><option value="CU">Cuba</option><option value="CY">Cyprus</option><option value="CZ">Czech Republic</option><option value="DK">Denmark</option><option value="DO">Dominican Republic</option><option value="EC">Ecuador</option><option value="EG">Egypt</option><option value="SV">El Salvador</option><option value="GQ">Equatorial Guinea</option><option value="EE">Estonia</option><option value="ET">Ethiopia</option><option value="FI">Finland</option><option value="FR">France</option><option value="GM">Gambia</option><option value="GE">Georgia</option><option value="DE">Germany</option><option value="GH">Ghana</option><option value="Гана">GHANA</option><option value="GR">Greece</option><option value="GT">Guatemala</option><option value="GY">Guyana</option><option value="HT">Haiti</option><option value="HN">Honduras</option><option value="HK">Hong Kong</option><option value="HU">Hungary</option><option value="IS">Iceland</option><option value="IN">India</option><option value="ID">Indonesia</option><option value="IR">Iran</option><option value="IQ">Iraq</option><option value="IE">Ireland, Republic Of</option><option value="IL">Israel</option><option value="IT">Italy</option><option value="JM">Jamaica</option><option value="JP">Japan</option><option value="JO">Jordan</option><option value="KZ">Kazakhstan</option><option value="KE">Kenya</option><option value="KP">Korea, Democratic Peoples Republic</option><option value="KR">Korea, Republic Of</option><option value="KW">Kuwait</option><option value="KG">Kyrgyzstan</option><option value="LV">Latvia</option><option value="LB">Lebanon</option><option value="LY">Libyan Arab Jamahiriya</option><option value="LT">Lithuania</option><option value="LU">Luxembourg</option><option value="MO">Macau</option><option value="MK">Macedonia</option><option value="MG">Madagascar (Malagasy)</option><option value="MY">Malaysia</option><option value="ML">Mali</option><option value="MT">Malta</option><option value="MU">Mauritius</option><option value="MX">Mexico</option><option value="MD">Moldova</option><option value="MC">Monaco</option><option value="MN">Mongolia</option><option value="ME">Montenegro</option><option value="MA">Morocco</option><option value="MZ">Mozambique</option><option value="NA">Namibia</option><option value="NP">Nepal</option><option value="NL">Netherlands</option><option value="NZ">New Zealand</option><option value="NI">Nicaragua</option><option value="NG">Nigeria</option><option value="NO">Norway</option><option value="PS">Occupied Palestinian Territory</option><option value="OM">Oman, Sultanate Of</option><option value="PK">Pakistan</option><option value="PA">Panama</option><option value="PY">Paraguay</option><option value="PE">Peru</option><option value="PH">Philippines</option><option value="PL">Poland</option><option value="PT">Portugal</option><option value="PR">Puerto Rico</option><option value="QA">Qatar</option><option value="RO">Romania</option><option value="RU">Russian Federation</option><option value="RW">Rwanda</option><option value="VC">Saint Vincent And The Grenadines</option><option value="SA">Saudi Arabia</option><option value="SN">Senegal</option><option value="RS">Serbia</option><option value="SL">Sierra Leone</option><option value="SG">Singapore</option><option value="SK">Slovakia</option><option value="SI">Slovenia</option><option value="ZA">South Africa Republic</option><option value="ES">Spain</option><option value="LK">Sri Lanka</option><option value="SE">Sweden</option><option value="CH">Switzerland</option><option value="SY">Syrian Arab Rep.</option><option value="TW">Taiwan, Republic of China</option><option value="TJ">Tajikistan</option><option value="TZ">Tanzania</option><option value="TH">Thailand</option><option value="TG">Togo</option><option value="TT">Trinidad and Tobago</option><option value="TN">Tunisia</option><option value="TR">Turkey</option><option value="TM">Turkmenistan</option><option value="UG">Uganda</option><option value="UA">Ukraine</option><option value="AE">United Arab Emirates</option><option value="GB">United Kingdom</option><option value="US">United States</option><option value="UY">Uruguay</option><option value="UZ">Uzbekistan</option><option value="VE">Venezuela</option><option value="VN">Vietnam</option><option value="YE">Yemen, Republic Of</option><option value="ZM">Zambia</option><option value="ZW">Zimbabwe</option><option value="zw">ZIMBABWE</option></select>
'''


def dump(path_to_file, text):
    f = None
    try:
        f = open(path_to_file, 'w')
        f.write(unicode(text))
    except:
        print 'Dump failed'
    finally:
        if f is not None:
            f.close()


def dump_json(path_to_file, data, sort_keys=True, indent=4):
    try:
        data_json = simplejson.dumps(data, sort_keys=sort_keys, indent=indent)
        dump(path_to_file, data_json)
    except:
        print 'Dump failed'


def extract__format_ott(lib_html, attrib_to_save, result):
    lib = etree.fromstring(lib_html)
    options = lib.findall('.//option')
    for option in options:
        code = option.attrib['value'].upper()
        value = option.text
        if len(code) > 2:
            print u'{} - incorrect code, value - {}'.format(code, value)
            continue
        if (code in result) and (attrib_to_save in result[code]):
            print u'{} - duplicate. Saved {}: {}, unsaved: {}'.format(
                code, attrib_to_save, result[code][attrib_to_save], value
            )
            continue
        if code not in result:
            result[code] = {
                'code': code,
                attrib_to_save: value
            }
        else:
            result[code].update({
                attrib_to_save: value
            })


if __name__ == '__main__':
    result = dict()
    extract__format_ott(citizenship_rus, 'name_ru', result)
    extract__format_ott(citizenship_eng, 'name_en', result)
    dump_json('/tmp/citizenship-ott.json', result.values())
