from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_solar_cells_efficiency_tables.schema_packages.mypackage import (
            m_package,
        )

        return m_package

mypackage = MySchemaPackageEntryPoint(
    name='MyPackage',
    description='Schema package defined using the new plugin mechanism.',
)

class EfficiencyTablesEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_solar_cells_efficiency_tables.schema_packages.efficiency_tables import (  # noqa: E501
            m_package,
        )

        return m_package


efficiency_tables = EfficiencyTablesEntryPoint(
    name='Efficiency Tables',
    description='Schema package data from efficiency tables of solar cells.',  # noqa: E501
)



