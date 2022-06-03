import argparse
import os

ans = "Working...\n--------------------------------------\n"
print(ans)

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', default='Человек', help="Имя пользователя")
parser.add_argument('-p', '--path', default='', help="Путь к файлу изображения")
parser.add_argument('-noQ', '--noQuest', action='store_true', help="Подавление вопросов пользователю")
args = parser.parse_args()


print(f'Привет, {args.name}!')


print(f'Проверяю путь к изображению: {args.path}...')
if os.path.exists(args.path):
    success = f'Файл {os.path.basename(args.path)} успешно удалён!'

    if args.noQuest:
        os.remove(args.path)
        print(success)
    else:
        ans = input(f'Удалить файл {os.path.basename(args.path)}?    Y/N: ').capitalize()
        if ans[0] == 'Y':
            os.remove(args.path)
            print(success)
        else:
            pass
else:
    print(f'Путь {args.path} не существует.')


ans = "\n--------------------------------------\n...End of work"
print(ans)