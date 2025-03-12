# sgpc-loader/

```markdown
├── alembic/
│   ├── versions/
│   │   ├── 67a54e557928_baseline.py
│   │   └── a08e81f1ab24_initial_migration.py
│   ├── README
│   ├── env.py
│   └── script.py.mako
├── documentation/
│   ├── app-flow.md
│   ├── backend-structure.md
│   ├── codebaseSummary.md
│   ├── currentTask.md
│   ├── prd.md
│   ├── projectRoadmap.md
│   ├── techStack.md
│   └── xlsx-ingestion-process.md
├── examples/
│   ├── check_invoice_exists.py
│   └── process_xlsx.py
├── invoices/
│   ├── FATURA.240120100054.TXT
│   └── excel_invoice.xlsx
├── logs/
├── migrations/
│   ├── 001_create_febraban_headers.sql
│   └── 002_create_cdrs_celular_raw.sql
├── scripts/
│   ├── db_script/
│   │   ├── FUNCTION_sgpc_schema.sql
│   │   ├── MVIEW_output.sql
│   │   ├── PACKAGE_output.sql
│   │   ├── SEQUENCE_sgpc_schema.sql
│   │   ├── functions_password.sql
│   │   └── tables.sql
│   ├── fix_models.py
│   └── setup_db.py
├── src/
│   └── febraban_loader/
│       ├── config/
│       │   ├── clients/
│       │   │   └── csn.yaml
│       │   └── config.yaml
│       ├── core/
│       │   ├── __init__.py
│       │   ├── base_processor.py
│       │   ├── enums.py
│       │   ├── exceptions.py
│       │   ├── header_processor.py
│       │   ├── models.py
│       │   ├── provider.py
│       │   ├── provider_manager.py
│       │   ├── provider_registry.py
│       │   ├── record_config.py
│       │   └── record_types.py
│       ├── db/
│       │   ├── models/
│       │   │   ├── __init__.py
│       │   │   ├── base.py
│       │   │   ├── billing.py
│       │   │   ├── cdrs_celular.py
│       │   │   ├── cdrs_celular_nf.py
│       │   │   ├── cdrs_celular_raw.py
│       │   │   ├── empresas.py
│       │   │   ├── extensions.py
│       │   │   ├── faturas.py
│       │   │   ├── febraban.py
│       │   │   ├── fornecedores.py
│       │   │   ├── grupos.py
│       │   │   ├── lines.py
│       │   │   ├── links.py
│       │   │   ├── localidades.py
│       │   │   ├── operadoras.py
│       │   │   ├── usuarios.py
│       │   │   ├── util.py
│       │   │   └── xlsx.py
│       │   ├── repositories/
│       │   │   ├── cdr.py
│       │   │   └── invoice.py
│       │   ├── __init__.py
│       │   └── connection.py
│       ├── providers/
│       │   ├── Febraban_v3_Mobile/
│       │   │   ├── config/
│       │   │   │   ├── 00_header.yaml
│       │   │   │   ├── 30_voice.yaml
│       │   │   │   ├── 40_services.yaml
│       │   │   │   ├── 70_adjustment.yaml
│       │   │   │   ├── 80_trailer.yaml
│       │   │   │   └── 90_info.yaml
│       │   │   ├── __init__.py
│       │   │   ├── processor.py
│       │   │   └── provider.yaml
│       │   ├── claro/
│       │   │   ├── config/
│       │   │   │   ├── 3_voice.yaml
│       │   │   │   ├── 4_services.yaml
│       │   │   │   ├── 7_adjustment.yaml
│       │   │   │   └── 8_trailer.yaml
│       │   │   ├── __init__.py
│       │   │   ├── processor.py
│       │   │   └── provider.yaml
│       │   ├── vivo/
│       │   │   ├── config/
│       │   │   │   ├── data.yaml
│       │   │   │   └── voice.yaml
│       │   │   ├── __init__.py
│       │   │   ├── processor.py
│       │   │   └── provider.yaml
│       │   ├── xlsx/
│       │   │   ├── config/
│       │   │   │   ├── 00_header.yaml
│       │   │   │   └── 30_voice.yaml
│       │   │   ├── __init__.py
│       │   │   ├── models.py
│       │   │   ├── processor.py
│       │   │   └── provider.yaml
│       │   └── __init__.py
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── invoice_utils.py
│       │   ├── transforms.py
│       │   └── validators.py
│       ├── __init__.py
│       ├── config.py
│       ├── get_header.py
│       ├── get_xlsx_header.py
│       └── old_cli.py
├── tests/
│   ├── providers/
│   ├── run_tests.sh
│   ├── test_db.py
│   ├── test_header_processor.py
│   └── test_models_pg.py
├── .gitignore
├── .pre-commit-config.yaml
├── .windsurfrules
├── README.md
├── alembic.ini
├── cli.py
├── pyproject.toml
└── requirements.txt
```
