import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    # Определяем участников и их силы
    participants = [
        ('Pasha', 3),
        ('Denis', 4),
        ('Apollon', 5),
    ]

    # Создаём задачи для каждого участника
    tasks = [start_strongman(name, power) for name, power in participants]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)


# Запускаем асинхронную функцию start_tournament
if __name__ == '__main__':
    asyncio.run(start_tournament())
