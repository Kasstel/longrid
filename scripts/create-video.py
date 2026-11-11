from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
out=Path('public/media')
font='C:/Windows/Fonts/arial.ttf'
bold='C:/Windows/Fonts/arialbd.ttf'
scenes=[
('01 / ПУТЕШЕСТВИЕ','Один маршрут. Разные системы.','Поиск → Бронирование → Оплата','Каждый участник хранит свою часть информации.'),
('02 / ОБЩИЙ РЕЕСТР','Записи получают связи.','Блок 01 → Блок 02 → Блок 03','Каждый следующий блок содержит хеш предыдущего.'),
('03 / СОГЛАСОВАННОСТЬ','Узлы проверяют правила.','Проверка → Консенсус → Общее состояние','Правила и доступ зависят от устройства сети.'),
('04 / СМАРТ-КОНТРАКТ','Событие становится условием.','Рейс → Оракул → Проверка условия','Внешние сведения поступают от источника данных.'),
('05 / ГРАНИЦЫ','Проверяемость ≠ истинность.','Данные на входе → Запись в реестре','Ложная информация не становится правдой в блокчейне.'),
('06 / ВЫВОД','Доверие — свойство всей системы.','ИИ + IoT + Блокчейн','Нужны проверка данных, поддержка и ответственность.')]
for i,(tag,title,flow,note) in enumerate(scenes):
 im=Image.new('RGB',(1280,720),'#0b1220');d=ImageDraw.Draw(im)
 for x in range(0,1280,80): d.line((x,0,x,720),fill='#14283b')
 for y in range(0,720,80): d.line((0,y,1280,y),fill='#14283b')
 d.text((72,60),'BLOCKCHAIN × TRAVEL',font=ImageFont.truetype(bold,18),fill='#a9bdcc')
 d.text((72,185),tag,font=ImageFont.truetype(font,18),fill='#29dccb')
 size=48
 while d.textlength(title,font=ImageFont.truetype(bold,size))>1136:size-=1
 d.text((72,245),title,font=ImageFont.truetype(bold,size),fill='#eff5f7')
 d.rounded_rectangle((72,355,1208,460),radius=4,fill='#172b46',outline='#29dccb')
 d.text((104,390),flow,font=ImageFont.truetype(font,30),fill='#29dccb')
 d.text((72,510),note,font=ImageFont.truetype(font,24),fill='#c1d1de')
 d.text((72,650),'Авторская объясняющая анимация · без звука · учебная иллюстрация',font=ImageFont.truetype(font,17),fill='#a9bdcc')
 d.rectangle((72,605,72+int(1136*(i+1)/6),608),fill='#29dccb')
 im.save(out/f'video-{i}.png')
 if i==0: im.save(out/'video-poster.webp',quality=85)
with (out/'explainer.vtt').open('w',encoding='utf-8') as f:
 f.write('WEBVTT\n\n')
 for i,(_,title,flow,note) in enumerate(scenes):
  start=i*10;end=start+10
  f.write(f'{i+1}\n00:{start//60:02}:{start%60:02}.000 --> 00:{end//60:02}:{end%60:02}.000\n{title}\n{note}\n\n')
