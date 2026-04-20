def format_name(full_name: str) -> str:

    parts = full_name.split()
    if len(parts) < 2:
        return full_name
    

    familiya = parts[0]
    ism_sharif = ' '.join(parts[1:])
    
    return f"{ism_sharif}, {familiya}"



if __name__ == "__main__":

    result1 = format_name("Aliyev Vali G'aniyevich")
    print(result1)  # "Vali G'aniyevich, Aliyev"
