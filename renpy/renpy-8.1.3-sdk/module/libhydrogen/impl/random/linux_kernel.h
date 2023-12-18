static int
hydro_random_init(void)
{
    get_random_bytes(&hydro_random_context.state,
        sizeof hydro_random_context.state);
    hydro_random_context.counter = ~LOAD64_LE(hydro_random_context.state);

    return 0;
}
