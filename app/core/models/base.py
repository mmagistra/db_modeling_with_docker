def get_db_migration_stmts():
    STMTS_FOR_MAGRATION = ["""
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
            FOREIGN KEY (fk_owner) REFERENCES owners(id_owner),
            FOREIGN KEY (fk_make_model) REFERENCES make_models(id_make_model)
        );
        """,
                           """
        
        CREATE TABLE IF NOT EXISTS public.orders (
            id_order SERIAL PRIMARY KEY NOT NULL,
            date DATE NOT NULL,
            fk_car INT NOT NULL,
            FOREIGN KEY (fk_car) REFERENCES cars(id_car)
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
            FOREIGN KEY (fk_order) REFERENCES orders(id_order),
            FOREIGN KEY (fk_work_type) REFERENCES work_types(id_work_type)
        );
        """]
    for stmt in STMTS_FOR_MAGRATION:
        yield stmt
