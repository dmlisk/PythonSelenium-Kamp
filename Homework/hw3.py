"""
HTML Nedir ?

Açılımı Hyper Text Markup Language  yani Hiper Metin İşaretleme Dili olan HTML,
web sayfalarını oluşturmak için kullanılan standart metin işaretleme dilidir.
Adından da anlaşılacağı üzere HTML bir programlama dili değildir.
Chrome, Firefox, Opera gibi web tarayıcıları HTML kodlarını işleyerek bu kodları web sayfalarına dönüştürür.

HTML, web tasarımcılarına sayfalar ve uygulamalar için yapı profilleri, bağlantılar, blok alıntılar,
paragraflar ve başlıklar oluşturmalarında yardımcıdır. Basit kod yapıları sayesinde web sayfaları şekillendirilebilir.
Ancak bilinmesi gereken en önemli şey HTML ile oluşturulan sitenin  dinamik değil statik olacağıdır.

HTML Locaters

Locators(Konumlandırıcı), Selenium IDE’ye hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir komuttur.
Doğru elementin tanımlanması, otomasyon oluşturmanın ön koşuludur.
Site üzerindeki bir elemente örneğin giriş butonuna selenium ile tıklama işlemi yaptırmak istediğimizde bu işlemi
locator’lar aracılığıyla yaparız. Selenium ile geliştirmek istediğimiz test otomasyonlarında locator’ları kullanarak ilgili
alanlara veri gönderebilir, tıklama işlemi yaptırabilir, var olan içeriği temizleyebiliriz.
En yaygın locator çeşitleri;

--> ID
--> Name
--> ClassName
--> TagName
--> LinkText
--> CssSelector
--> XPath

Selenium

get() --> Verilen Url’e Erişme
maximize_window() --> Tarayıcıyı Tam Ekran Yapmak
quit() --> Quit komutuyla açık olan tarayıcımızı kapatabiliriz.
click() --> Seçilen öğeye tıklamak için kullanılır.
clear() --> Seçilen öğenin içeriğini temizlemek için kullanılır.
submit() --> Göndermek için kullanılır.
back() --> Bir önceki sayfaya gitmek için kullanılır.
forward() --> Bir sonraki sayfaya gitmek için kullanılır.
Refresh() --> Sayfayı yenilemek için kullanılır.
Selenium’da elementleri bulmak ve seçmek için birçok yöntem var bunlar :
Xpath Yöntemi : find_element_by_xpath()
ID Yöntemi : find_element_by_id()
Name Yöntemi : find_element_by_name()
Link Text Yöntemi : find_element_by_link_text()
TagName Yöntemi : find_element_by_tag_name()
Class Name Yöntemi : find_element_by_class_name()
CSS Selector Yöntemi : find_element_by_css_selector()
Partial Link Text Yöntemi : find_element_by_partial_link_text()


"""