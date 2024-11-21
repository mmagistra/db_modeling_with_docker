--
-- PostgreSQL database dump
--

-- Dumped from database version 14.8
-- Dumped by pg_dump version 14.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: work_types; Type: TABLE; Schema: public; Owner: mmagistr
--

CREATE TABLE public.work_types (
    id_work_type integer NOT NULL,
    name character varying(32) NOT NULL,
    price numeric(10,2) NOT NULL
);


ALTER TABLE public.work_types OWNER TO mmagistr;

--
-- Name: WorkTypes_id_work_type_seq; Type: SEQUENCE; Schema: public; Owner: mmagistr
--

CREATE SEQUENCE public."WorkTypes_id_work_type_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."WorkTypes_id_work_type_seq" OWNER TO mmagistr;

--
-- Name: WorkTypes_id_work_type_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mmagistr
--

ALTER SEQUENCE public."WorkTypes_id_work_type_seq" OWNED BY public.work_types.id_work_type;


--
-- Name: cars; Type: TABLE; Schema: public; Owner: mmagistr
--

CREATE TABLE public.cars (
    id_car integer NOT NULL,
    fk_owner integer NOT NULL,
    release_year integer,
    car_number character varying(6) NOT NULL,
    fk_make_model integer NOT NULL,
    CONSTRAINT cars_release_year_check CHECK ((release_year >= 1885))
);


ALTER TABLE public.cars OWNER TO mmagistr;

--
-- Name: cars_id_car_seq; Type: SEQUENCE; Schema: public; Owner: mmagistr
--

CREATE SEQUENCE public.cars_id_car_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cars_id_car_seq OWNER TO mmagistr;

--
-- Name: cars_id_car_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mmagistr
--

ALTER SEQUENCE public.cars_id_car_seq OWNED BY public.cars.id_car;


--
-- Name: make_model; Type: TABLE; Schema: public; Owner: mmagistr
--

CREATE TABLE public.make_model (
    id_make_model integer NOT NULL,
    make_model character varying(16) NOT NULL
);


ALTER TABLE public.make_model OWNER TO mmagistr;

--
-- Name: makemodel_id_make_model_seq; Type: SEQUENCE; Schema: public; Owner: mmagistr
--

CREATE SEQUENCE public.makemodel_id_make_model_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.makemodel_id_make_model_seq OWNER TO mmagistr;

--
-- Name: makemodel_id_make_model_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mmagistr
--

ALTER SEQUENCE public.makemodel_id_make_model_seq OWNED BY public.make_model.id_make_model;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: mmagistr
--

CREATE TABLE public.orders (
    id_order integer NOT NULL,
    date date NOT NULL,
    fk_car integer NOT NULL
);


ALTER TABLE public.orders OWNER TO mmagistr;

--
-- Name: orders_id_order_seq; Type: SEQUENCE; Schema: public; Owner: mmagistr
--

CREATE SEQUENCE public.orders_id_order_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_id_order_seq OWNER TO mmagistr;

--
-- Name: orders_id_order_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mmagistr
--

ALTER SEQUENCE public.orders_id_order_seq OWNED BY public.orders.id_order;


--
-- Name: owners; Type: TABLE; Schema: public; Owner: mmagistr
--

CREATE TABLE public.owners (
    id_owner integer NOT NULL,
    name character varying(32) NOT NULL,
    phone_number character varying(16) NOT NULL
);


ALTER TABLE public.owners OWNER TO mmagistr;

--
-- Name: owners_id_owner_seq; Type: SEQUENCE; Schema: public; Owner: mmagistr
--

CREATE SEQUENCE public.owners_id_owner_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.owners_id_owner_seq OWNER TO mmagistr;

--
-- Name: owners_id_owner_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mmagistr
--

ALTER SEQUENCE public.owners_id_owner_seq OWNED BY public.owners.id_owner;


--
-- Name: works_in_order; Type: TABLE; Schema: public; Owner: mmagistr
--

CREATE TABLE public.works_in_order (
    id_work_in_order integer NOT NULL,
    fk_order integer NOT NULL,
    fk_work_type integer NOT NULL,
    work_number integer NOT NULL,
    count integer NOT NULL,
    amount numeric(10,2) NOT NULL,
    CONSTRAINT worksinorder_amount_check CHECK ((amount >= (0)::numeric)),
    CONSTRAINT worksinorder_count_check CHECK ((count > 0)),
    CONSTRAINT worksinorder_work_number_check CHECK ((work_number > 0))
);


ALTER TABLE public.works_in_order OWNER TO mmagistr;

--
-- Name: worksinorder_id_work_in_order_seq; Type: SEQUENCE; Schema: public; Owner: mmagistr
--

CREATE SEQUENCE public.worksinorder_id_work_in_order_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.worksinorder_id_work_in_order_seq OWNER TO mmagistr;

--
-- Name: worksinorder_id_work_in_order_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mmagistr
--

ALTER SEQUENCE public.worksinorder_id_work_in_order_seq OWNED BY public.works_in_order.id_work_in_order;


--
-- Name: cars id_car; Type: DEFAULT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.cars ALTER COLUMN id_car SET DEFAULT nextval('public.cars_id_car_seq'::regclass);


--
-- Name: make_model id_make_model; Type: DEFAULT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.make_model ALTER COLUMN id_make_model SET DEFAULT nextval('public.makemodel_id_make_model_seq'::regclass);


--
-- Name: orders id_order; Type: DEFAULT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.orders ALTER COLUMN id_order SET DEFAULT nextval('public.orders_id_order_seq'::regclass);


--
-- Name: owners id_owner; Type: DEFAULT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.owners ALTER COLUMN id_owner SET DEFAULT nextval('public.owners_id_owner_seq'::regclass);


--
-- Name: work_types id_work_type; Type: DEFAULT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.work_types ALTER COLUMN id_work_type SET DEFAULT nextval('public."WorkTypes_id_work_type_seq"'::regclass);


--
-- Name: works_in_order id_work_in_order; Type: DEFAULT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.works_in_order ALTER COLUMN id_work_in_order SET DEFAULT nextval('public.worksinorder_id_work_in_order_seq'::regclass);


--
-- Data for Name: cars; Type: TABLE DATA; Schema: public; Owner: mmagistr
--

COPY public.cars (id_car, fk_owner, release_year, car_number, fk_make_model) FROM stdin;
1	1	2015	A123BC	1
2	2	2018	D456EF	2
3	3	2020	G789HI	3
4	4	2017	J012KL	4
5	5	2019	M345NO	5
\.


--
-- Data for Name: make_model; Type: TABLE DATA; Schema: public; Owner: mmagistr
--

COPY public.make_model (id_make_model, make_model) FROM stdin;
1	Toyota Camry
2	Honda Accord
3	Ford Focus
5	Audi A4
4	BMW X5
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: mmagistr
--

COPY public.orders (id_order, date, fk_car) FROM stdin;
1	2023-01-15	1
2	2023-02-20	2
3	2023-03-10	3
4	2023-04-05	4
5	2023-05-25	5
\.


--
-- Data for Name: owners; Type: TABLE DATA; Schema: public; Owner: mmagistr
--

COPY public.owners (id_owner, name, phone_number) FROM stdin;
1	╨Ш╨▓╨░╨╜ ╨Ш╨▓╨░╨╜╨╛╨▓ ╨Ш╨▓╨░╨╜╨╛╨▓╨╕╤З	1234567890
2	╨Я╨╡╤В╤А ╨Я╨╡╤В╤А╨╛╨▓ ╨Я╨╡╤В╤А╨╛╨▓╨╕╤З	0987654321
3	╨б╨╡╤А╨│╨╡╨╣ ╨б╨╡╤А╨│╨╡╨╡╨▓ ╨б╨╡╤А╨│╨╡╨╡╨▓╨╕╤З	1122334455
4	╨Р╨╗╨╡╨║╤Б╨╡╨╣ ╨Р╨╗╨╡╨║╤Б╨╡╨╡╨▓ ╨Р╨╗╨╡╨║╤Б╨╡╨╡╨▓╨╕╤З	2233445566
5	╨Ь╨░╤А╨╕╤П ╨Ь╨░╤А╨╕╨╡╨▓╨░ ╨Ь╨░╤А╤М╨╡╨▓╨╜╨░	3344556677
\.


--
-- Data for Name: work_types; Type: TABLE DATA; Schema: public; Owner: mmagistr
--

COPY public.work_types (id_work_type, name, price) FROM stdin;
1	╨Ч╨░╨╝╨╡╨╜╨░ ╨╝╨░╤Б╨╗╨░	1500.00
2	╨а╨╡╨╝╨╛╨╜╤В ╨┤╨▓╨╕╨│╨░╤В╨╡╨╗╤П	25000.00
3	╨Ч╨░╨╝╨╡╨╜╨░ ╤В╨╛╤А╨╝╨╛╨╖╨╛╨▓	8000.00
4	╨и╨╕╨╜╨╛╨╝╨╛╨╜╤В╨░╨╢	3000.00
5	╨Я╨╛╨╗╨╕╤А╨╛╨▓╨║╨░ ╨║╤Г╨╖╨╛╨▓╨░	5000.00
\.


--
-- Data for Name: works_in_order; Type: TABLE DATA; Schema: public; Owner: mmagistr
--

COPY public.works_in_order (id_work_in_order, fk_order, fk_work_type, work_number, count, amount) FROM stdin;
1	1	1	1	1	1500.00
2	2	2	1	1	25000.00
3	3	3	1	2	16000.00
4	4	4	1	1	3000.00
5	5	5	1	1	5000.00
\.


--
-- Name: WorkTypes_id_work_type_seq; Type: SEQUENCE SET; Schema: public; Owner: mmagistr
--

SELECT pg_catalog.setval('public."WorkTypes_id_work_type_seq"', 5, true);


--
-- Name: cars_id_car_seq; Type: SEQUENCE SET; Schema: public; Owner: mmagistr
--

SELECT pg_catalog.setval('public.cars_id_car_seq', 5, true);


--
-- Name: makemodel_id_make_model_seq; Type: SEQUENCE SET; Schema: public; Owner: mmagistr
--

SELECT pg_catalog.setval('public.makemodel_id_make_model_seq', 5, true);


--
-- Name: orders_id_order_seq; Type: SEQUENCE SET; Schema: public; Owner: mmagistr
--

SELECT pg_catalog.setval('public.orders_id_order_seq', 5, true);


--
-- Name: owners_id_owner_seq; Type: SEQUENCE SET; Schema: public; Owner: mmagistr
--

SELECT pg_catalog.setval('public.owners_id_owner_seq', 5, true);


--
-- Name: worksinorder_id_work_in_order_seq; Type: SEQUENCE SET; Schema: public; Owner: mmagistr
--

SELECT pg_catalog.setval('public.worksinorder_id_work_in_order_seq', 5, true);


--
-- Name: work_types WorkTypes_pkey; Type: CONSTRAINT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.work_types
    ADD CONSTRAINT "WorkTypes_pkey" PRIMARY KEY (id_work_type);


--
-- Name: cars cars_pkey; Type: CONSTRAINT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.cars
    ADD CONSTRAINT cars_pkey PRIMARY KEY (id_car);


--
-- Name: make_model makemodel_pkey; Type: CONSTRAINT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.make_model
    ADD CONSTRAINT makemodel_pkey PRIMARY KEY (id_make_model);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id_order);


--
-- Name: owners owners_pkey; Type: CONSTRAINT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.owners
    ADD CONSTRAINT owners_pkey PRIMARY KEY (id_owner);


--
-- Name: works_in_order worksinorder_pkey; Type: CONSTRAINT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.works_in_order
    ADD CONSTRAINT worksinorder_pkey PRIMARY KEY (id_work_in_order);


--
-- Name: cars cars_fk_make_model_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.cars
    ADD CONSTRAINT cars_fk_make_model_fkey FOREIGN KEY (fk_make_model) REFERENCES public.make_model(id_make_model);


--
-- Name: cars cars_fk_owner_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.cars
    ADD CONSTRAINT cars_fk_owner_fkey FOREIGN KEY (fk_owner) REFERENCES public.owners(id_owner);


--
-- Name: orders orders_fk_car_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_fk_car_fkey FOREIGN KEY (fk_car) REFERENCES public.cars(id_car);


--
-- Name: works_in_order worksinorder_fk_order_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.works_in_order
    ADD CONSTRAINT worksinorder_fk_order_fkey FOREIGN KEY (fk_order) REFERENCES public.orders(id_order);


--
-- Name: works_in_order worksinorder_fk_work_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mmagistr
--

ALTER TABLE ONLY public.works_in_order
    ADD CONSTRAINT worksinorder_fk_work_type_fkey FOREIGN KEY (fk_work_type) REFERENCES public.work_types(id_work_type);


--
-- PostgreSQL database dump complete
--

