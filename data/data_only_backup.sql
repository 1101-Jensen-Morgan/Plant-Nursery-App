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

--
-- Data for Name: care; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.care (id, lighting, watering, soil, temperature, humidity, pet_safe) FROM stdin;
1	 Bright light	Sandy, acidic soil, such as a cactus potting medium	Allow the plant to dry out between waterings.	55-85	40%	f
2	Bright, indirect light (though can handle low light)	Moist, well-draining soil	Let the soil dry out between waterings.	65 to 75	50 to 70%	t
3	Bright, indirect light	Light well-draining soil, especially a mix made for succulents or cacti	Let the soil dry out between waterings.	70 to 90	30 to 50%	f
4	Bright, indirect light	Light well-draining soil with bark, moss, or peat	Let the soil dry out between waterings.	50 to 90	 40 to 70%	f
5	 Indirect light	Moist well-draining soil	Let the soil dry out between waterings.	65 to 80	50 to 70%	t
6	Bright sunlight	Moist, well-draining soil	Keep the soil moist and mist occasionally.	70	50 to 70%	f
7	Bright, indirect light	Moist well-draining soil	Keep the soil moist.	70	50 to 70%	f
8	Bright, indirect light	Light well-draining soil (preferably a succulent-specific blend)	Keep soil moist in spring and summer and water monthly in winter.	60 to 75	30 to 50%	f
9	Bright to moderate indirect light	Loamy, well-draining soil	Let the top 2 inches of soil dry out between waterings.	50 to 90	50 to 70%	f
10	Bright, indirect light	Light well-draining soil	Keep the plant moist with regular watering.	60 to 75	30 to 50%	f
11	Bright, indirect light	Light well-draining soil	Keep the soil moist with regular watering.	65 to 75	50 to 70%	t
12	Bright, indirect light	Well-draining peat-based soil	Keep the soil moist with regular watering during the spring and winter; water occasionally in the fall and winter.	65 to 75	50 to 70%	f
13	Bright full sunlight	Dry well-draining soil (a cactus blend is ideal)	Let the top of the soil dry out between waterings, with biweekly misting.	50 to 80	40 to 70%	f
14	Bright, indirect light	Rich, moist soil	Let the soil dry between waterings before a good soak; misting is required during spring and summer.	60 to 80	50 to 70%	t
15	Bright, indirect light	Rich, well-draining soil	Water when the top inch of soil is dry, less frequently during the winter.	65 to 75	50 to 70%	f
16	Bright to moderate indirect light	Rich, well-drained potting soil or water	Use bottled or distilled water, and change the water in the vase weekly.	65 to 90	30 to 50%	f
17	Moderate indirect light	Moist, well-draining soil	Let the top of the soil dry between waterings.	70 to 90	30 to 50%	f
18	Bright, indirect light	Well-draining soil	Let the soil dry out completely between waterings.	50 to 90	30 to 50%	f
19	Bright, indirect light	Rich well-draining soil with peat and perlite	Water frequently to keep the soil moist (but not soaked); reduce the watering schedule during the fall and winter.	65 to 75	Over 80%	f
20	Bright, indirect light	Peaty, well-draining soil	Let the soil dry out between waterings.	65 to 75	40 to 70%	f
21	Bright, indirect light	Light well-draining soil	Water when the top inch of soil is dry.	60 to 85	30 to 65%	t
22	Bright to moderate indirect light	Rich well-draining soil	Let the soil dry out between waterings.	50 to 90	30 to 50%	f
23	Bright, indirect light	Fast-draining soil, or grown as an air plant	Water into the center of the plant, or by lightly moistening the soil.	60 to 85	40 to 50%	f
24	Bright to moderate indirect light	Light well-draining soil	Let soil dry out between waterings	70 to 80	30 to 50%	t
25	Bright, indirect light	Sandy, succulent, or cactus potting soil	Water weekly or biweekly to keep lightly moist.	50 to 90	30 to 50%	t
26	Bright, indirect light	Light well-draining soil	Keep soil moist during summer and drier during the winter.	60 to 80	40 to 80%	f
27	Indirect light or low light	Light well-draining soil	Let the soil dry out between waterings.	70 to 90	50 to 70%	f
28	Bright sunlight	Sandy, cactus, or succulent soil	Water weekly to biweekly during the spring and summer and monthly during the winter.	60 to 90	30 to 50%	f
29	Bright, indirect light	Rich well-draining soil	Let the soil dry out at least 2 inches down between waterings.	50 to 80	40 to 70%	f
30	Bright, indirect light	Light well-draining soil, especially a succulent or cactus blend	Let the soil dry out 1 to 2 inches between waterings.	60 to 80	30 to 50%	f
31	Bright, indirect light	Well-draining soil with bark, perlite, or peat	Let the top half inch of soil dry out between waterings.	60 to 75	40 to 60%	f
32	Bright, indirect light	Soilless potting mix	Allow to dry to the touch before watering.	60 to 80	40%	f
33	Bright, indirect sunlight	Well-draining soil	Keep moist but not wet; mist often.	65 to 85	50 to 60%	f
34	Bright, indirect sunlight	Light potting soil or sandy loam	Allow to dry completely, then soak; do not mist.	70 to 80	20 to 50%	f
35	Bright, indirect sunlight	Coarse, well-draining	Keep moist but not soaked; mist occasionally.	55 to 85	60 to 75%	f
36	Bright, indirect sunlight	Light, well-draining soil	Keep moist but not soaked; mist often.	70 to 90	65 to 80%	f
37	Bright, indirect sunlight	Light, well-draining soil	Keep moist but not soaked; mist often.	65 and 80	40 to 60%	f
38	Bright, indirect light	Light well-draining soil	Keep moist but not soaked; mist often.	60 to 90	50 to 70%	f
39	Bright, indirect light	Airy, well-draining soil	Allow to dry completely, then soak; mist occasionally.	60 to 80	40 to 70%	f
\.


--
-- Data for Name: plant_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.plant_info (id, commonname, latinname, description) FROM stdin;
1	Aloe Vera	Aloe Vera	spiky and low maintenance
2	Golden Pothos 	Epipremnum aureum	A vine with  medium sized leaves. Also called the devils vine or devils ivy
3	Snake Plant	Dracaena trifasciata	Also known as mother-in-laws tongue, devils tongue, or sansevieria. Has loong leaves with a snake-like patern and stands upright
4	Moth Orchid	Phalaenopsis amabilis	A flowering plant, whose flowers have vibrant colors. It also has wide, rubbery leaves.
5	Peace Lily	Spathiphyllum wallisii	A flowering plant whose white blooms last for weeks. It also has vibrant, glossy leaves.
6	Basil	Ocimum Basilicum	A very leafy , fragrent herb that many use as a garnish or to add flavor to many dishes
7	African Violet	Saintpaulia Ionantha	A flowering house plant with small purple blooms that appear several times a year.
8	Jade Plant	Crassula Ovata	A green succulent with numerous rounded leaves.
9	Spider Plant	Chlorophytum Comosum	A plant with long, flexible, slender leaves that have a while stripe along the center. When thriving, they often produce ofspring that can be snipped and replanted.
10	Rubber Plant	Ficus Elastica	A tropical plant with wide rubbery leaves, as the name suggests. It also has the ability to grow into a tree.
11	Dumb Cane Plant	Dieffenbachia	A plant with wide leave that have a wide range of unique patterns. These plants can be grown into trees.
12	Monstera Deliciosa	Monstera Deliciosa	Also known as a Swiss cheese plant, it has very large leaves with several holes, and a unique shape.
13	Rosemary	Salvia Rosmarinus	An herb with several stems containing numerous small leaves. Its fragrence and distinct flavor make it a great garnish or ingredient in many dishes.
14	Umbrella Plant	Schefflera Actinophylla	A tropical plant that has numerous leaves at the end of each branch that droop down, making an umbrella shape. This plant also tends to grow quickly.
15	Money Tree	Guiana Chestnut	Also known as a Guina chestnut, this plant bosts large, starshaped leaves and a braided trunk.
16	Lucky Bamboo	Dracaena Sanderiana	This plant has a sturdy, unique trunk with a few large leaves at the top.
17	English Ivy	Hedera helix	This vine has a green and white pattern on its leaves. Its trailing behavior makes it a great hanging plant.
18	ZZ Plant	Zamioculcas Zamiifolia	This plant features dark green leaves that go all the way up each stem.
19	Boston Fern	Nephrolepis Exaltata	This plant has many tiny leaves that go along each stem
20	Areca Palms	Dypsis Lutescens	A comparatively large palm tree that can grow up to 8 ft tall.
21	Fiddle Leaf Fig	Ficus Lyrata	A plant very large, wide leaves. This plant is infamous for being very difficult to care for.
22	Pilea	Pilea Peperomioides	Also known as a Chinese monay plant, it has several round leaves.
23	Bromeliads	Bromeliaceae	This plant has very colorful blooms and very long slender leaves. They are also extremely hardy and easy to care for.
24	Dragon Tree	Dracaena Marginata	This plants many long, thin, drooping leaves gives it a spiky look. This is also very easy to care for.
25	String of Pearls	Curio Rowleyanus	This succulent has numerous balls that trail all the way down each stem. The stems of this plant are also very long, making it a very good canidate for a hanging plant.
26	Croton	Codiaeum Variegatum	This tropical plant has very bright colors and unique patterns on its leaves.
27	Chinese Evergreen	Aglaonema Commutatum	This plant boasts many different color and patern variations and can serve as a natural air purifier. Additionally If you choose a Chinese evergreen with bright or variegated leaves, you will need to keep it in a brighter spot to maintain the coloring, while green varieties do well in low light.
28	Ponytail Palm	Beaucarnea Recurvata	These trees have shaggy leaves and thick, woody truncks. They are slow growing but can eventually become tree sized.
29	Oyster Plant	Tradescantia Spathacea	This small plant has colorful leaves with green and purple colorings.
30	Kalanchoe	Kalanchoe blossfeldiana	This succulent has several very colorful blooms.
31	Jasmine Plant	Jasminum	This plant has beautiful, fragrant flowers. Some varieties of this plant are vines, which makes them good hanging plants.
32	Heartleaf Philodendron	Philodendron Hederaceum	This plant has heart shaped leaves and is also known as the sweatheart plant. It is also very fast growing and vining.
33	Silver Leaf Philodendron	Philodendron Brandtianum	This vining, epiphytic, highly-sought-after species can be trained to grow up, rooting into a moist surface, or simply allowed to cascade out of a pot or hanging basket
34	Polka Dot Begonia	Begonia Maculata	the begonia maculata grows on a cane-like stem with long emerald green leaves and a smattering of silver spots. The back of the leaf is red, and the plant flowers with dense clusters of white blooms. It is also known to be a difficult plant to care for.
35	Black Velvet Alocasia	Alocasia Reginula	This plant has large, saturated green leaves contrasted with white vining.
36	Birds Nest Anthurium	Anthurium Superbum	Colloquially known as a birds nest anthurium (not to be confused with the birds nest fern) the dazzling anthurium superbum is recognized by its waffled, shiny, ironclad leaves. Some distinctive characteristics are its bronze-colored new foliage and beefy, above-soil structural roots.
37	Ficus Audrey	Ficus benghalensis	Ficus Audrey has deep green, oval-shaped leaves with dramatic yellow veins.
38	Homalomena Selby	Homalomena hybrid	This plant has leaves with rich yellow and gree tones and ornate markings.
39	Sweetheart Plant	Hoya Kerrii	This is a vining suculent that has a heart-shaped design.
\.


--
-- Data for Name: plants_owned; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.plants_owned (id, user_id, plant_id) FROM stdin;
1	1	1
2	1	6
3	1	31
4	2	28
5	2	20
6	1	2
7	8	39
8	8	9
9	8	4
10	9	1
11	9	8
12	9	26
13	10	6
14	10	13
15	10	16
16	10	11
17	11	37
18	11	34
19	11	15
20	11	21
21	12	7
22	12	10
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, username, password, firstname, lastname) FROM stdin;
1	bol	1234	Billy	Bob
2	gip	web	Wild	Nugget
3	mor	abds	Morgan	Jensen
6	katy	3456	Kate	Johnson
7	magni	nugge4t	John	Doe
8	Sparky82	SecurePassword123	Emily	Johnson
9	TechNinja23	NinjaMaster456	Marcus	Lee
10	LunaStar77	Starlight2024	Sofia	Rodriguez
11	PixelPioneer	PixelPower2024	Ryan	Thompson
12	QuantumCoder	Quantum123Code	Emma	Martin
\.


--
-- Data for Name: watering_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.watering_log (id, date, amountw, fertilizer, amountf, user_id, plant_id) FROM stdin;
1	2024-01-05	20	f	0	1	1
2	2024-05-01	24	t	6	1	6
3	2024-05-01	16	f	0	1	2
4	2024-05-01	8	t	4	1	3
5	2024-05-01	14	t	6	1	31
6	2024-05-03	15	f	0	1	2
7	2024-04-18	6	f	0	1	31
8	2024-05-04	16	f	0	8	39
9	2024-05-04	16	f	0	8	9
10	2024-05-04	6	t	1	8	4
11	2024-04-27	18	f	0	8	39
12	2024-04-27	10	t	6	8	9
13	2024-04-20	10	f	0	8	4
14	2024-05-04	8	f	0	9	1
15	2024-05-04	8	f	0	9	8
16	2024-05-04	10	f	0	9	26
17	2024-04-04	8	f	0	9	1
18	2024-04-04	6	f	0	9	8
19	2024-04-27	8	f	0	9	26
20	2024-05-04	24	f	0	10	6
21	2024-05-04	8	f	0	10	13
22	2024-05-04	30	f	0	10	16
23	2024-05-04	8	t	3	10	11
24	2024-04-20	24	f	0	10	6
25	2024-04-27	12	f	0	10	13
26	2024-03-23	30	f	0	10	16
27	2024-04-27	8	f	0	10	11
28	2024-05-04	8	f	0	11	37
29	2024-05-04	8	f	0	11	34
30	2024-05-04	8	f	0	11	15
31	2024-05-04	8	f	0	11	21
32	2024-05-04	30	f	0	11	37
33	2024-05-11	30	f	0	11	15
34	2024-05-18	30	t	12	11	21
35	2024-05-11	10	f	0	11	34
36	2024-05-04	12	t	6	12	7
37	2024-05-04	8	f	0	12	10
38	2024-04-29	12	f	0	12	7
39	2024-04-27	12	t	6	12	10
\.


--
-- PostgreSQL database dump complete
--

