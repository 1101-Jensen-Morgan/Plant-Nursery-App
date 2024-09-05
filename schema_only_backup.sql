--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

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
-- Name: care; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.care (
    id integer,
    lighting character varying(255),
    watering character varying(255),
    soil character varying(225),
    temperature character varying(20),
    humidity character varying(20),
    pet_safe boolean
);


ALTER TABLE public.care OWNER TO postgres;

--
-- Name: plant_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.plant_info (
    id integer,
    commonname character varying(255),
    latinname character varying(255),
    description character varying(500)
);


ALTER TABLE public.plant_info OWNER TO postgres;

--
-- Name: plants_owned; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.plants_owned (
    id integer,
    user_id integer,
    plant_id integer
);


ALTER TABLE public.plants_owned OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer,
    username character varying(80),
    password character varying(30),
    firstname character varying(80),
    lastname character varying(80)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: watering_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.watering_log (
    id integer,
    date date,
    amountw double precision,
    fertilizer boolean,
    amountf double precision,
    user_id integer,
    plant_id integer
);


ALTER TABLE public.watering_log OWNER TO postgres;

--
-- PostgreSQL database dump complete
--

