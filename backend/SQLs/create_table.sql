CREATE TABLE public.users
(
    user_id serial NOT NULL ,
    user_name character varying(50) NOT NULL,
    user_password character varying(255) NOT NULL,
    createdtime timestamp with time zone NOT NULL,
    CONSTRAINT "PK" PRIMARY KEY (user_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to emma;