import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN", "8326589244:AAFKkEw7Dg0WqFhc89DtwQhkureSR4y4mY8")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Полный каталог со всеми 23 историями
CATALOG = {
    "1": {
        "name": "1. Индивидуальные браслеты",
        "items": {
            "individual": {
                "name": "Индивидуальные браслеты",
                "link": "https://t.me/yoursecrettemptation/138"
            }
        }
    },
    "2": {
        "name": "2. Летние ожерелья",
        "items": {
            "kannikuly": {
                "name": "Ожерелье «Каникулы на острове»",
                "link": "https://t.me/yoursecrettemptation/255"
            },
            "first_love": {
                "name": "Ожерелье «Первая любовь»",
                "link": "https://t.me/yoursecrettemptation/257"
            },
            "daisies": {
                "name": "Ожерелье «Поле с ромашками»",
                "link": "https://t.me/yoursecrettemptation/259"
            }
        }
    },
    "3": {
        "name": "3. Достижения",
        "items": {
            "green_flag": {
                "name": "Браслет «Грин Флаг»",
                "link": "https://t.me/yoursecrettemptation/577"
            },
            "women_energy": {
                "name": "Браслет «Женская Энергия»",
                "link": "https://t.me/yoursecrettemptation/580"
            },
            "crosses_ruler": {
                "name": "Ожерелье «Повелительница Крестов»",
                "link": "https://t.me/yoursecrettemptation/582"
            },
            "yst_thief": {
                "name": "Ожерелье «Расхитительница YST»",
                "link": "https://t.me/yoursecrettemptation/584"
            },
            "fool_genius": {
                "name": "Браслет «Шут – Гений»",
                "link": "https://t.me/yoursecrettemptation/707"
            },
            "mama_alice": {
                "name": "Браслет «Мама-Алиса»",
                "link": "https://t.me/yoursecrettemptation/710"
            },
            "star_remy": {
                "name": "Браслет «Звезда-Реми»",
                "link": "https://t.me/yoursecrettemptation/713"
            }
        }
    },
    "4": {
        "name": "4. Секрет Небес",
        "items": {
            "lucifer": {
                "name": "Браслет «Люцифер»",
                "link": "https://t.me/yoursecrettemptation/51"
            },
            "malbonte": {
                "name": "Браслет «Мальбонте»",
                "link": "https://t.me/yoursecrettemptation/47"
            },
            "golod": {
                "name": "Браслет «Голод»",
                "link": "https://t.me/yoursecrettemptation/114"
            },
            "mimi": {
                "name": "Браслет «Мими»",
                "link": "https://t.me/yoursecrettemptation/236"
            }
        }
    },
    "5": {
        "name": "5. Секрет Небес. Реквием",
        "items": {
            "angel_secret": {
                "name": "Ожерелье «Секрет Ангела»",
                "link": "https://t.me/yoursecrettemptation/284"
            },
            "boris_gift": {
                "name": "Ожерелье «Подарок Бориса»",
                "link": "https://t.me/yoursecrettemptation/376"
            },
            "dmitry": {
                "name": "Браслет «Дмитрий»",
                "link": "https://t.me/yoursecrettemptation/379"
            },
            "boris": {
                "name": "Браслет «Борис»",
                "link": "https://t.me/yoursecrettemptation/385"
            },
            "kain": {
                "name": "Браслет «Каин»",
                "link": "https://t.me/yoursecrettemptation/394"
            },
            "yan": {
                "name": "Браслет «Ян»",
                "link": "https://t.me/yoursecrettemptation/494"
            },
            "lein": {
                "name": "Браслет «Лэйн»",
                "link": "https://t.me/yoursecrettemptation/491"
            },
            "rings_set": {
                "name": "Набор Колечек «Секрет Небес: Реквием»",
                "link": "https://t.me/yoursecrettemptation/563"
            },
            "memories": {
                "name": "Парные ожерелья «Воспоминания о Роткове»",
                "link": "https://t.me/yoursecrettemptation/413"
            },
            "full_set": {
                "name": "Обвес «Секрет Небес: Реквием»",
                "link": "https://t.me/yoursecrettemptation/722"
            }
        }
    },
    "6": {
        "name": "6. Разбитое Сердце Астреи",
        "items": {
            "cassiel": {
                "name": "Браслет «Кассиэль»",
                "link": "https://t.me/yoursecrettemptation/382"
            },
            "david": {
                "name": "Браслет «Давид»",
                "link": "https://t.me/yoursecrettemptation/397"
            },
            "malek": {
                "name": "Браслет «Малек»",
                "link": "https://t.me/yoursecrettemptation/497"
            },
            "rafael": {
                "name": "Браслет «Рафаил»",
                "link": "https://t.me/yoursecrettemptation/500"
            },
            "rose_queen": {
                "name": "Ожерелье «Королева Роз»",
                "link": "https://t.me/yoursecrettemptation/503"
            }
        }
    },
    "7": {
        "name": "7. Сага о Грозах",
        "items": {
            "sharnez": {
                "name": "Браслет «Ша'арнез»",
                "link": "https://t.me/yoursecrettemptation/485"
            },
            "tai": {
                "name": "Браслет «Тай»",
                "link": "https://t.me/yoursecrettemptation/488"
            },
            "saga": {
                "name": "Ожерелье «Сага о Грозах»",
                "link": "https://t.me/yoursecrettemptation/569"
            }
        }
    },
    "8": {
        "name": "8. Пришествие Номер Три",
        "items": {
            "ksandr": {
                "name": "Браслет «Ксандр»",
                "link": "https://t.me/yoursecrettemptation/695"
            }
        }
    },
    "9": {
        "name": "9. Шифр Шекспира",
        "items": {
            "edward": {
                "name": "Браслет «Эдвард»",
                "link": "https://t.me/yoursecrettemptation/700"
            },
            "hobello": {
                "name": "Браслет «Хобелло»",
                "link": "https://t.me/yoursecrettemptation/701"
            },
            "ralph": {
                "name": "Браслет «Ральф»",
                "link": "https://t.me/yoursecrettemptation/704"
            }
        }
    },
    "10": {
        "name": "10. Песнь о Красном Ниле",
        "items": {
            "amen": {
                "name": "Браслет «Амен»",
                "link": "https://t.me/yoursecrettemptation/54"
            },
            "liviy": {
                "name": "Браслет «Ливий»",
                "link": "https://t.me/yoursecrettemptation/57"
            },
            "protection": {
                "name": "Ожерелье «Защита Амена»",
                "link": "https://t.me/yoursecrettemptation/62"
            },
            "set": {
                "name": "Браслет «Сет»",
                "link": "https://t.me/yoursecrettemptation/233"
            },
            "sunmoon": {
                "name": "Парные ожерелья «Солнце и Луна»",
                "link": "https://t.me/yoursecrettemptation/410"
            }
        }
    },
    "11": {
        "name": "11. И Поглотит Нас Морок",
        "items": {
            "volot": {
                "name": "Браслет «Волот»",
                "link": "https://t.me/yoursecrettemptation/388"
            },
            "ozar": {
                "name": "Браслет «Озар»",
                "link": "https://t.me/yoursecrettemptation/391"
            },
            "morok": {
                "name": "Ожерелье «И Поглотит Нас Морок»",
                "link": "https://t.me/yoursecrettemptation/574"
            }
        }
    },
    "12": {
        "name": "12. Кали - Зов Тьмы",
        "items": {
            "reytan": {
                "name": "Браслет «Рэйтан»",
                "link": "https://t.me/yoursecrettemptation/41"
            },
            "liliya": {
                "name": "Ожерелье «Поцелуй Лилии»",
                "link": "https://t.me/yoursecrettemptation/299"
            },
            "amrit": {
                "name": "Браслет «Амрит»",
                "link": "https://t.me/yoursecrettemptation/44"
            },
            "amrita_amala": {
                "name": "Парные браслеты «Любовь Амрита и Амалы»",
                "link": "https://t.me/yoursecrettemptation/152"
            },
            "kali_rings": {
                "name": "Набор Колечек «Кали»",
                "link": "https://t.me/yoursecrettemptation/565"
            }
        }
    },
    "13": {
        "name": "13. Кали - Пламя Сансары",
        "items": {
            "ram": {
                "name": "Браслет «Рам»",
                "link": "https://t.me/yoursecrettemptation/287"
            },
            "saraswati": {
                "name": "Браслет «Сарасвати»",
                "link": "https://t.me/yoursecrettemptation/302"
            },
            "kali_sansara_rings": {
                "name": "Набор Колечек «Кали»",
                "link": "https://t.me/yoursecrettemptation/565"
            }
        }
    },
    "14": {
        "name": "14. Цветок из Огня Тиамат",
        "items": {
            "dragon_secret": {
                "name": "Ожерелье «Тайна Дракона»",
                "link": "https://t.me/yoursecrettemptation/60"
            },
            "kingu": {
                "name": "Браслет «Кингу»",
                "link": "https://t.me/yoursecrettemptation/242"
            },
            "niall": {
                "name": "Браслет «Ниалл»",
                "link": "https://t.me/yoursecrettemptation/239"
            }
        }
    },
    "15": {
        "name": "15. Дракула. История Любви",
        "items": {
            "dracula": {
                "name": "Браслет «Дракула»",
                "link": "https://t.me/yoursecrettemptation/117"
            }
        }
    },
    "16": {
        "name": "16. Легенда Ивы",
        "items": {
            "kazu": {
                "name": "Браслет «Кадзу»",
                "link": "https://t.me/yoursecrettemptation/111"
            },
            "iwa_set": {
                "name": "Обвес «Легенда Ивы»",
                "link": "https://t.me/yoursecrettemptation/721"
            }
        }
    },
    "17": {
        "name": "17. Я Охочусь на Тебя",
        "items": {
            "love_alexander_agata": {
                "name": "Парные браслеты «Любовь Александра и Агаты»",
                "link": "https://t.me/yoursecrettemptation/146"
            }
        }
    },
    "18": {
        "name": "18. Арканум",
        "items": {
            "love_liam_selena": {
                "name": "Парные браслеты «Любовь Лиама и Селены»",
                "link": "https://t.me/yoursecrettemptation/149"
            },
            "liam": {
                "name": "Браслет «Лиам»",
                "link": "https://t.me/yoursecrettemptation/247"
            },
            "arkanuma_set": {
                "name": "Обвес «Арканум»",
                "link": "https://t.me/yoursecrettemptation/718"
            }
        }
    },
    "19": {
        "name": "19. Пси Ψ",
        "items": {
            "jonas": {
                "name": "Браслет «Йонас»",
                "link": "https://t.me/yoursecrettemptation/203"
            },
            "inquisitor_love": {
                "name": "Ожерелье «Любовь Инквизитора»",
                "link": "https://t.me/yoursecrettemptation/206"
            },
            "psi": {
                "name": "Ожерелье «Пси»",
                "link": "https://t.me/yoursecrettemptation/571"
            },
            "psi_rings": {
                "name": "Набор Колечек «Пси»",
                "link": "https://t.me/yoursecrettemptation/567"
            }
        }
    },
    "20": {
        "name": "20. Роза Пустыни",
        "items": {
            "adil": {
                "name": "Браслет «Адиль»",
                "link": "https://t.me/yoursecrettemptation/200"
            },
            "zein": {
                "name": "Браслет «Зейн»",
                "link": "https://t.me/yoursecrettemptation/249"
            }
        }
    },
    "21": {
        "name": "21. Теодора",
        "items": {
            "lawrence": {
                "name": "Браслет «Лоуренс»",
                "link": "https://t.me/yoursecrettemptation/290"
            },
            "friedrich": {
                "name": "Браслет «Фридрих»",
                "link": "https://t.me/yoursecrettemptation/296"
            }
        }
    },
    "22": {
        "name": "22. Ловчая Времени",
        "items": {
            "onyx": {
                "name": "Браслет «Оникс»",
                "link": "https://t.me/yoursecrettemptation/293"
            }
        }
    },
    "23": {
        "name": "23. Рождённая Луной",
        "items": {
            "victor": {
                "name": "Браслет «Виктор»",
                "link": "https://t.me/yoursecrettemptation/189"
            }
        }
    }
}


@dp.message(CommandStart())
async def start(message: Message):
    greeting = (
        "Привет! Добро пожаловать в YST – место, где натуральные камни оживают "
        "в виде частички любимого персонажа💖\n\n"
        "В этом боте можно выбрать украшение по персонажу💋\n\n"
        "Выбери историю ниже👇"
    )
    await message.answer(greeting)
    await show_categories(message)


async def show_categories(message: Message):
    text = "✨ Выбери историю, по которой хочешь посмотреть украшение:"
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=CATALOG[cat]["name"], 
                callback_data=f"cat_{cat}"
            )]
            for cat in sorted(CATALOG.keys(), key=lambda x: int(x))
        ]
    )
    await message.answer(text, reply_markup=keyboard)


@dp.callback_query(F.data.startswith("cat_"))
async def show_items(callback: CallbackQuery):
    category_id = callback.data.replace("cat_", "")
    
    if category_id not in CATALOG:
        await callback.answer("❌ Категория не найдена", show_alert=True)
        return
    
    category = CATALOG[category_id]
    text = f"📌 {category['name']}\n\nВыбери украшение:"
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=category["items"][item]["name"],
                callback_data=f"item_{category_id}_{item}"
            )]
            for item in category["items"]
        ] + [
            [InlineKeyboardButton(text="⬅️ Назад к историям", callback_data="back_menu")]
        ]
    )
    
    await callback.message.edit_text(text, reply_markup=keyboard)
    await callback.answer()


@dp.callback_query(F.data.startswith("item_"))
async def show_item_details(callback: CallbackQuery):
    data = callback.data.replace("item_", "")
    parts = data.split("_", 1)
    
    if len(parts) != 2:
        await callback.answer("❌ Ошибка", show_alert=True)
        return
    
    category_id, item_id = parts
    
    if category_id not in CATALOG or item_id not in CATALOG[category_id]["items"]:
        await callback.answer("❌ Товар не найден", show_alert=True)
        return
    
    item = CATALOG[category_id]["items"][item_id]
    link = item["link"]
    
    text = (
        f"💎 {item['name']}\n\n"
        f"⭐️ Посмотреть украшение и прочитать описание можно в этом посте – {link}\n"
        f"⭐️ Чтобы приобрести украшение, напишите в @yst_supportt"
    )
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Открыть пост", url=link)],
            [InlineKeyboardButton(text="⬅️ Назад к украшениям", callback_data=f"cat_{category_id}")]
        ]
    )
    
    await callback.message.edit_text(text, reply_markup=keyboard)
    await callback.answer()


@dp.callback_query(F.data == "back_menu")
async def back_to_menu(callback: CallbackQuery):
    text = "✨ Выбери историю, по которой хочешь посмотреть украшение:"
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=CATALOG[cat]["name"], 
                callback_data=f"cat_{cat}"
            )]
            for cat in sorted(CATALOG.keys(), key=lambda x: int(x))
        ]
    )
    await callback.message.edit_text(text, reply_markup=keyboard)
    await callback.answer()


async def main():
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
