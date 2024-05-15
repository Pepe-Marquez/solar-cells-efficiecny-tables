def test_importing_app():
    # this will raise an exception if pydantic model validation fails for th app
    from nomad_solar_cells_efficiency_tables.apps import myapp
