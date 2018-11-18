FROM python:3

EXPOSE 80

ENV SECRET_KEY=dId_you_r3aLly_think_I_w0u1dnt_s3t_a_key
ENV RANDOM_SEED=oh_n0_u_foUnD_mY_s3ed
ENV ADMIN_PASS=sUp3r_n0t_secR3t_aDm1n_paSsw0rD

WORKDIR /clicker2.0/clicker2.0
ADD . /clicker2.0

RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "startup.sh"]
