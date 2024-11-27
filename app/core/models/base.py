def get_db_migration_stmts():
    STMTS_FOR_MAGRATION = [
        """
        CREATE TABLE IF NOT EXISTS public."work_types"
        (
            id_work_type serial,
            name character varying(32) NOT NULL,
            price numeric(10, 2) NOT NULL,
            PRIMARY KEY (id_work_type)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS public.owners (
            id_owner SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(32) NOT NULL,
            phone_number VARCHAR(16) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS public.make_models (
            id_make_model SERIAL PRIMARY KEY NOT NULL,
            make_model VARCHAR(16) NOT NULL
        );
        """,
        """
        
        CREATE TABLE IF NOT EXISTS public.cars (
            id_car SERIAL PRIMARY KEY NOT NULL,
            fk_owner INT NOT NULL,
            release_year INT CHECK (release_year >= 1885),
            car_number VARCHAR(6) NOT NULL,
            fk_make_model INT NOT NULL,
            FOREIGN KEY (fk_owner) REFERENCES owners(id_owner) ON DELETE CASCADE,
            FOREIGN KEY (fk_make_model) REFERENCES make_models(id_make_model) ON DELETE CASCADE
        );
        """,
        """
        
        CREATE TABLE IF NOT EXISTS public.orders (
            id_order SERIAL PRIMARY KEY NOT NULL,
            date DATE NOT NULL,
            fk_car INT NOT NULL,
            FOREIGN KEY (fk_car) REFERENCES cars(id_car) ON DELETE CASCADE
        );
        """,
        """
        
        CREATE TABLE IF NOT EXISTS public.works_in_order (
            id_work_in_order SERIAL PRIMARY KEY NOT NULL,
            fk_order INT NOT NULL,
            fk_work_type INT NOT NULL,
            work_number INT NOT NULL CHECK (work_number > 0),
            count INT NOT NULL CHECK (count > 0),
            amount NUMERIC(10, 2) NOT NULL CHECK (amount >= 0),
            FOREIGN KEY (fk_order) REFERENCES orders(id_order) ON DELETE CASCADE,
            FOREIGN KEY (fk_work_type) REFERENCES work_types(id_work_type) ON DELETE CASCADE
        );
        """]
    for stmt in STMTS_FOR_MAGRATION:
        yield stmt


def get_default_data_insert_stmts():
    INSERT_STMTS = [
        """
        -- Заполнение данными
        -- Добавление данных в таблицу work_types
        INSERT INTO public."work_types" (name, price) VALUES
        ('Замена масла', 1500.00),
        ('Ремонт двигателя', 25000.00),
        ('Замена тормозов', 8000.00),
        ('Шиномонтаж', 3000.00),
        ('Полировка кузова', 5000.00);
        """,
        """
        -- Добавление данных в таблицу owners
        INSERT INTO public.owners (name, phone_number) VALUES
        ('Иван Иванов Иванович', '1234567890'),
        ('Петр Петров Петрович', '0987654321'),
        ('Сергей Сергеев Сергеевич', '1122334455'),
        ('Алексей Алексеев Алексеевич', '2233445566'),
        ('Мария Мариева Марьевна
        ', '3344556677');
        """,
        """
        -- Добавление данных в таблицу make_model
        INSERT INTO public.make_model (make_model) VALUES
        ('Toyota Camry'),
        ('Honda Accord'),
        ('Ford Focus'),
        ('BMW 3 Series'),
        ('Audi A4');
        """,
        """
        -- Добавление данных в таблицу cars
        INSERT INTO public.cars (fk_owner, release_year, car_number, fk_make_model) VALUES
        (1, 2015, 'A123BC', 1),
        (2, 2018, 'D456EF', 2),
        (3, 2020, 'G789HI', 3),
        (4, 2017, 'J012KL', 4),
        (5, 2019, 'M345NO', 5);
        """,
        """
        -- Добавление данных в таблицу orders
        INSERT INTO public.orders (date, fk_car) VALUES
        ('2023-01-15', 1),
        ('2023-02-20', 2),
        ('2023-03-10', 3),
        ('2023-04-05', 4),
        ('2023-05-25', 5);
        """,
        """
        -- Добавление данных в таблицу works_in_order
        INSERT INTO public.works_in_order (fk_order, fk_work_type, work_number, count, amount) VALUES
        (1, 1, 1, 1, 1500.00),
        (2, 2, 1, 1, 25000.00),
        (3, 3, 1, 2, 16000.00),
        (4, 4, 1, 1, 3000.00),
        (5, 5, 1, 1, 5000.00);
        """
    ]
    for stmt in INSERT_STMTS:
        yield stmt