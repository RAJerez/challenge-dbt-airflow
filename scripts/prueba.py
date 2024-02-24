from cfg import delimiter

paths_dict = {
    "venta" : 1,
    "producto" : 2,
    "cliente" : 3,
    "tipo_gasto" : 4,
    "proveedor" : 5,
    "sucursal" : 6,
    "empleado" : 7,
    "gasto" : 8,
}

for name, file in paths_dict.items():
    if name in delimiter: sep = ";"
    else: sep = ","
    print(f"The separator of the {name} table is {sep}")
    
#    try:
#        RawLoader(name).load_table(file_path, sep)
#        print(f"Data {name} loaded correctly")
#    
#    except exc.SQLAlchemyError as e:
        # SQLAlchemy Specific Errors
#        print(f"Error loading data {name}: {e}")
#    
#    except Exception as e:
#        # General exceptions
#        print(f"Unexpected error: {e}")