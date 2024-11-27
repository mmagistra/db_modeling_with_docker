"""
-- Заполнение данными
-- Добавление данных в таблицу work_types
INSERT INTO public."work_types" (id_work_type, name, price) VALUES
(1, 'Замена масла', 1500.00),
(2, 'Ремонт двигателя', 25000.00),
(3, 'Замена тормозов', 8000.00),
(4, 'Шиномонтаж', 3000.00),
(5, 'Полировка кузова', 5000.00);

-- Добавление данных в таблицу owners
INSERT INTO public.owners (id_owner, name, phone_number) VALUES
(1, 'Иван Иванов Иванович', '1234567890'),
(2, 'Петр Петров Петрович', '0987654321'),
(3, 'Сергей Сергеев Сергеевич', '1122334455'),
(4, 'Алексей Алексеев Алексеевич', '2233445566'),
(5, 'Мария Мариева Марьевна
', '3344556677');

-- Добавление данных в таблицу make_model
INSERT INTO public.make_models (id_make_model, make_model) VALUES
(1, 'Toyota Camry'),
(2, 'Honda Accord'),
(3, 'Ford Focus'),
(4, 'BMW 3 Series'),
(5, 'Audi A4');

-- Добавление данных в таблицу cars
INSERT INTO public.cars (id_car, fk_owner, release_year, car_number, fk_make_model) VALUES
(1, 1, 2015, 'A123BC', 1),
(2, 2, 2018, 'D456EF', 2),
(3, 3, 2020, 'G789HI', 3),
(4, 4, 2017, 'J012KL', 4),
(5, 5, 2019, 'M345NO', 5);

-- Добавление данных в таблицу orders
INSERT INTO public.orders (id_order, date, fk_car) VALUES
(1, '2023-01-15', 1),
(2, '2023-02-20', 2),
(3, '2023-03-10', 3),
(4, '2023-04-05', 4),
(5, '2023-05-25', 5);

-- Добавление данных в таблицу works_in_order
INSERT INTO public.works_in_order (id_work_in_order, fk_order, fk_work_type, work_number, count, amount) VALUES
(1, 1, 1, 1, 1, 1500.00),
(2, 2, 2, 1, 1, 25000.00),
(3, 3, 3, 1, 2, 16000.00),
(4, 4, 4, 1, 1, 3000.00),
(5, 5, 5, 1, 1, 5000.00);
"""