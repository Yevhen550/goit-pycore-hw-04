def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:

            for line in file:
                cat = line.strip().split(",")
                cat_info = {"id": cat[0], "name": cat[1], "age": cat[2]}
                cats_info.append(cat_info)

        return cats_info

    except FileNotFoundError:
        return f"Файл не знайдено"


all_cats_info = get_cats_info("2-task/cats_file.txt")
print(all_cats_info)
