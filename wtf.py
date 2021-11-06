import os
import kivy
kivy.require('1.4.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
class MyApp(App):
    Window.clearcolor = (1, 1, 1, 1)
    Window.minimum_width = 270
    Window.minimum_height = 480
    Window.fullscreen = 0 #можно заменить на 0 и чекнуть c компа как оно на телефоне будет выглядеть 'auto'
    def build(self):
        path = os.path.dirname(os.path.abspath(__file__))
        layout = BoxLayout(padding=-30, orientation='vertical')
        carousel = Carousel(loop=True)
        carousel.add_widget(Label(size_hint=(None, None), size=(250, 250), font_name='Times', text='[color=000000]Тульская обл.,г.Сергиев\n Посад,спу.Ленина,30\nДорожное покрытие\nДыра в асфальте\n около второго дома\nлезут демоны третий день[/color]', markup=True))
        carousel.add_widget(Label(size_hint=(None, None), size=(250, 250), font_name='Times', text='[color=000000]Тамб.обл.,г.Ногинск,\nул.Будапештсткая,23\nБезопасность\nПереодические сходки\n на детской площадке[/color]', markup=True))#типо подключенная база данных
        carousel.add_widget(Label(size_hint=(None, None), size=(250, 250), font_name='Times', text='[color=000000]Белг. обл.,г.Истра,\nпр.Будапештсткая,59\nКомуникации\nНе работает\n городской телефон[/color]', markup=True))
        carousel.add_widget(Label(size_hint=(None, None), size=(250, 250), font_name='Times', text='[color=000000]Кем.область,г.Луховицы,\nпер.Сталина,92\nДомостроение\nОбрушился фасад\n здания[/color]', markup=True))
        carousel.add_widget(Label(size_hint=(None, None), size=(250, 250), font_name='Times', text='[color=000000]Курс.обл.,г.Пушкино,\nвъе.Косиора,53\nДругое\nДикие собаки\n каждый вечер[/color]', markup=True))
        carousel.add_widget(Label(size_hint=(None, None), size=(250, 250), font_name='Times', text='[color=000000]Влад.обл.,г.Чехов,\nшос.Гоголя,52\nКомуникации\nЭлектрические щитки\n убивают людей[/color]', markup=True))
        carousel.add_widget(Label(size_hint=(None, None), size=(250, 250), font_name='Times', text='[color=000000]Влад.обл.,г.Чехов,\nшос.Гоголя,23\nСоциальная\nВ универмаге24/7 продают\n табак и алкоголь детям[/color]', markup=True))
        carousel.add_widget(Label(size_hint=(None, None), size=(250, 250), font_name='Times', text='[color=000000]Омск.обл.,г.Красногорск,\nпр.Косиора,83\nДорожное покрытие\nПобитые заборы[/color]', markup=True))
        carousel.add_widget(Label(size_hint=(None, None), size=(250, 250), font_name='Times', text='[color=000000]Нижегор.обл.,г.Подольск,\nпр.Домодедовская,4\nДругое\nПтицы разносят\n невывезенный мусор[/color]', markup=True))
        carousel.add_widget(Label(size_hint=(None, None), size=(250, 250), font_name='Times', text='[color=000000]Сарат.обл.,г.Серебряные\n Пруды,про.Космонавтов,91\nДомостроение\nПротечка крыши[/color]', markup=True))
        img_top = Image(source=path + '\Main_menu_top.png',
                        size_hint=(1, 0.28))
        img_bottom = Image(source=path + '\Main_menu_tottom.png',
                           size_hint=(1, 1.25))
        layout.add_widget(img_top)
        layout.add_widget(carousel)
        layout.add_widget(img_bottom)
        return layout
if __name__ == '__main__':
    MyApp().run()