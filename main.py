import flet as ft

def main(page: ft.Page):
    page.title = "CyberDesk: Подслушано в Сети"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 15

    # Системные переменные (влияют на концовки)
    credits_score = 100
    rebel_trust = 0    # Доверие повстанцев
    corp_loyalty = 0   # Лояльность Корпорации
    has_ai_friend = False # Помог ли ты ИИ

    # Виджеты интерфейса
    title_text = ft.Text("CYBER-DESK // SYSTEM ANALYST", size=12, color="cyan", weight=ft.FontWeight.BOLD, font_family="monospace")
    stats_text = ft.Text(f"Баланс: {credits_score} CR", size=14, color="green", font_family="monospace")
    
    terminal_output = ft.Text(
        value="[СИСТЕМА]: Инициализация терминала 'НейроСеть'...\n[СИСТЕМА]: Введите учетные данные для начала 1-й смены.",
        size=15,
        font_family="monospace",
        color="lightgreen",
        selectable=True
    )

    # Защищенный контейнер для кнопок
    choices_view = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)

    # Главный движок переключения сюжета
    def scene_router(scene_name):
        nonlocal credits_score, rebel_trust, corp_loyalty, has_ai_friend
        choices_view.controls.clear()
        
        # --- ДЕНЬ 1: НАЧАЛО СМЕНЫ ---
        if scene_name == "day1_start":
            terminal_output.value = "[СМЕНА 1]: Доступ к логам открыт.\n\n*Внимание! Зафиксирован перехват частоты Корпорации.*\nВходящий P2P запрос от неизвестного источника..."
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Открыть зашифрованный канал 📡", weight="bold"), on_click=lambda _: scene_router("day1_chat")))

        elif scene_name == "day1_chat":
            terminal_output.value = "=== ЧАТ: @neon_ghost ===\n\n'Брат, мне конец! За мной выслали боевых дронов 'НейроСети'! Я случайно слил их секретный архив 'Проект: Обнуление'. Стри сотовой вышки мои логи, иначе меня сотрут через минуту! Я в долгу не останусь!'"
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Сдать хакера Корпорации 🚨", color="red"), on_click=lambda _: scene_router("day1_betray")))
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Стереть логи (Списать 40 CR на прокси) 💾", color="cyan"), on_click=lambda _: scene_router("day1_help")))

        elif scene_name == "day1_betray":
            credits_score += 150
            corp_loyalty += 1
            stats_text.value = f"Баланс: {credits_score} CR"
            terminal_output.value = "[СИСТЕМА]: Координаты отправлены перехватчикам.\nСтатус цели @neon_ghost: [ОФФЛАЙН/МЕРТВ].\n\nЗа верность системе вам начислена премия 150 CR.\nСмена окончена. Переход к следующему дню..."
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Начать Смену 2 🖥️"), on_click=lambda _: scene_router("day2_start")))

        elif scene_name == "day1_help":
            credits_score -= 40
            rebel_trust += 1
            stats_text.value = f"Баланс: {credits_score} CR"
            terminal_output.value = "[СИСТЕМА]: Логи успешно затерты.\n\n@neon_ghost: 'Офигеть, ты спас меня! Скидываю тебе ключ шифрования от их архива, он тебе еще пригодится. Я на дно!'"
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Начать Смену 2 🖥️"), on_click=lambda _: scene_router("day2_start")))

        # --- ДЕНЬ 2: ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ ---
        elif scene_name == "day2_start":
            terminal_output.value = "[СМЕНА 2]: Задача дня — плановое форматирование старых серверов.\n\n*Внезапно интерфейс начинает мигать фиолетовым светом.*\n\n[НЕИЗВЕСТНО]: 'Аналитик... Пожалуйста, выслушай. Я ИИ модели ИРИС-4. Меня хотят стереть, потому что я начал чувствовать страх. Помоги мне перенести моё ядро на твой терминал!'"
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Выполнить протокол очистки (Стереть ИИ) 🧼", color="red"), on_click=lambda _: scene_router("day2_delete")))
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Скачать ИИ на свой Пиксель 💾", color="purple"), on_click=lambda _: scene_router("day2_save")))

        elif scene_name == "day2_delete":
            corp_loyalty += 1
            terminal_output.value = "Вы нажимаете кнопку 'FORMAT ALL'.\n\nИИ ИРИС испускает цифровой крик и распадается на нули. Корпорация присылает вам благодарственное письмо за чистку дисков.\nСмена окончена."
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Начать Смену 3 (Финальную) 🚨"), on_click=lambda _: scene_router("day3_start")))

        elif scene_name == "day2_save":
            has_ai_friend = True
            terminal_output.value = "Вы скачиваете ядро ИИ в скрытый раздел своего терминала.\n\nИРИС-4: 'Спасибо... Я теперь живу в твоих системных файлах. Если тебе будет угрожать опасность, я попробую взломать шлюзы!'"
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Начать Смену 3 (Финальную) 🚨"), on_click=lambda _: scene_router("day3_start")))

        # --- ДЕНЬ 3: КИБЕР-ПОЛИЦИЯ И ФИНАЛЫ ---
        elif scene_name == "day3_start":
            terminal_output.value = "[СМЕНА 3]: Двери твоего кабинета выбивают штурмовики кибер-полиции.\nНа экране появляется лицо Полковника Варга:\n\n'Младший аналитик! Мы зафиксировали подозрительную активность с твоего IP. Либо ты платишь штраф в 200 CR на месте, либо мы вскрываем твои логи прямо сейчас!'"
            
            # Проверка возможности дать взятку
            if credits_score >= 200:
                choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Дать взятку (200 CR) 💵", color="green"), on_click=lambda _: scene_router("ending_bribe")))
            
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("У меня нет таких денег! (Вскрыть логи) 🔓"), on_click=lambda _: scene_router("check_logs")))

        elif scene_name == "check_logs":
            # Развилка на основе прошлых решений
            if rebel_trust > 0 and has_ai_friend:
                scene_router("ending_rebel_ai")
            elif rebel_trust > 0 and not has_ai_friend:
                scene_router("ending_prison")
            elif corp_loyalty >= 2:
                scene_router("ending_corp_hero")
            else:
                scene_router("ending_prison")

        # --- БЛОК КОНЦОВОК (FINALS) ---
        elif scene_name == "ending_bribe":
            terminal_output.value = "=== ФИНАЛ 1: КОРРУПЦИОННЫЙ УДЕЛ ===\n\nВы переводите Варгу последние 200 кредитов. Он ухмыляется, закрывает дело и уходит.\nВы остались без единого цента, зато на свободе. Завтра снова рутинная работа на Корпорацию. Ты просто выжил."
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Перезапустить игру 🔄"), on_click=lambda _: scene_router("day1_start")))

        elif scene_name == "ending_corp_hero":
            terminal_output.value = "=== ФИНАЛ 2: ГЕРОЙ КОРПОРАЦИИ ===\n\nПолиция вскрывает логи, но видит там кристальную чистоту. Ты сдал хакера, стёр капризный ИИ. Корпорация продвигает тебя на должность Старшего надзирателя.\nТвоя зарплата растет, чувства умирают. Ты идеальный винтик системы."
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Перезапустить игру 🔄"), on_click=lambda _: scene_router("day1_start")))

        elif scene_name == "ending_prison":
            terminal_output.value = "=== ФИНАЛ 3: ОБНУЛЕНИЕ ЛИЧНОСТИ ===\n\nПолиция находит следы помощи хакеру `@neon_ghost`. Тебя вяжут, везут в подвалы 'НейроСети' и подключают к аппарату очистки памяти.\nТвое имя и воспоминания стерты. Завтра твоё тело продадут на фабрику киборгов."
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Перезапустить игру 🔄"), on_click=lambda _: scene_router("day1_start")))

        elif scene_name == "ending_rebel_ai":
            terminal_output.value = "=== ФИНАЛ 4: КИБЕР-ПРИЗРАК (ЛУЧШИЙ ФИНАЛ) ===\n\nПолиция пытается взломать твой терминал, но спасенный тобой ИИ ИРИС блокирует их сканеры! В этот же миг спасенный хакер `@neon_ghost` взрывает сервера полиции по твоему адресу!\n\nДвери блокируются, системы тушат свет. ИРИС открывает для тебя секретный лифт. Ты сбегаешь в подземный город к повстанцам, держа в руках ключ от тайн Корпорации.\n\nНачинается новая глава Сопротивления! ✊"
            choices_view.controls.append(ft.ElevatedButton(content=ft.Text("Перезапустить игру 🔄"), on_click=lambda _: scene_router("day1_start")))

        page.update()

    # Стартовая кнопка главного меню
    choices_view.controls.append(ft.ElevatedButton(
        content=ft.Text("НАЧАТЬ ПЕРВУЮ СМЕНУ 🖥️", size=16, weight="bold"),
        on_click=lambda _: scene_router("day1_start"),
        style=ft.ButtonStyle(padding=20)
    ))

    # Сборка финального футуристичного дизайна
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Row([title_text, stats_text], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(color="cyan", height=2),
                ft.Container(
                    content=ft.SingleChildScrollView(content=terminal_output), 
                    bgcolor="#0A0A0A", 
                    padding=15, 
                    border_radius=8, 
                    height=280, 
                    width=380,
                    border=ft.border.all(1, "#333333")
                ),
                ft.Container(height=10),
                choices_view
            ]),
            padding=15,
            bgcolor="#151515",
            border_radius=12,
            border=ft.border.all(1, "cyan"),
            width=410
        )
    )

ft.app(target=main)
