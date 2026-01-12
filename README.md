# Sage Alerting → Telegram Notifications

Проект демонстрирует настройку **системы алертов в Sage** с автоматической отправкой уведомлений в **Telegram-канал** при нарушении ключевых метрик.


## Цель

Настроить оповещения (alerts) в Sage так, чтобы при деградации **системных метрик** и **метрик пробера** уведомления автоматически отправлялись в Telegram.

## Реализация

- Создан **Telegram-канал** для группы (получатель алертов)
- В Sage настроен **Destination / Address** для отправки уведомлений в Telegram
- Созданы алерты:
  - **2 системных**
  - **2 проберных**
  - **алерт на JavaScript**
- Проведена демонстрация срабатывания алерта (rule → firing → Telegram)


## Архитектура

1. **Sage собирает метрики**
   - системные: CPU, RAM и т.п.
   - probe: availability/latency
2. **Alert Rules** отслеживают нарушения порогов/условий
3. При `FIRING` уведомление отправляется в **Destination (Telegram Channel)**


## Настройка Telegram Destination в Sage

1. Создать Telegram-канал для группы
2. В Sage перейти в `Notifications / Destinations`
3. Создать Destination:
   - `Name`: `tg_group_<group>`
   - `Type`: `Telegram`
   - `Recipient`: Telegram Channel (username/id)
4. Сохранить Destination и использовать его в alert rules


## Демонстрация срабатывания

Сценарий:
1. Создано условие деградации метрики (нагрузка / отказ / рост latency)
2. Alert Rule перешёл в состояние `FIRING`
3. Sage отправил уведомление в Destination
4. Сообщение появилось в Telegram-канале
