class ClashRoyale

    def self.menu
        puts "\n"
        puts "1.- Mostrar la Tabla   " +"   2.- Agregar elemento     " +"               3.- Buscar Registro "
        puts "4.- Elimina un Registro" +"   5.- Eliminar Todos los Registros    " +"    6.- Ordenar los Rgistros" +  "          0.- Salir "        
        ClashRoyale.opciones
    end 

    def self.opciones        
        opcion= gets.chomp

        if opcion == "1"
            ClashRoyale.opcion1
        elsif opcion == "2"
            ClashRoyale.opcion2
        elsif opcion == "3"
            ClashRoyale.opcion3
        elsif 
            opcion == "4"
            ClashRoyale.opcion4
        elsif 
            opcion == "5"
            ClashRoyale.opcion5
        elsif
            opcion == "6"        
            ClashRoyale.opcion6
        elsif opcion == "0"
            puts "salir"
        else
            puts "opcion no valida, Ingresa una entrada valida "
            estado = 0
            if estado == 0
                ClashRoyale.menu
            end 
        end 
    end

    def self.opcion1            
        str= "Muestra la Tabla"
        puts str.rjust  300        
    content = File.readlines 'Cartas.Clash'
#    content.each_with_index{|line, i| puts "#{i+1}: #{line}"}
     contenido = IO.readlines('Cartas.Clash')
     puts contenido               
        ClashRoyale.menu
    end 
            
            def self.opcion2

                puts "Ingresa una carta disponible"
                puts "\ncartas disponibles: "
                disponible = ["Esbirros", "Dragon", "Esqueletos", "Valkyria", "Caballero", "Peka", "Minero", "Mago", "Tesla", "Espejo", "Tronco", "Princesa", "Zap", "Lenador", "Espiritu", "Furia"]
                puts disponible            
                puts "\nNombre: "
            @name= gets.chomp.capitalize
                resnombre= disponible.include? @name        
                    if resnombre == true                                                                   
                        ClashRoyale.type
                    else 
                        puts "Lo siento esa carta no existe aún\n".rjust 310
                        ClashRoyale.opcion2            
                    end        
            end 

            def self.type                
                tipo= "\nIngresa la calidad de la  carta: " + @name 
                puts tipo
                typedisponible = ["Comun", "Rara", "Epica", "Legendaria"]           
                puts "1.-Comun", "2.-Rara", "3.-Epica", "4.-Legendaria"
                type = gets.chomp.capitalize
                    if type == "1"
                        @type = "Comun" 
                    elsif  type == "2"
                        @type = "Rara"
                    elsif type == "3"
                        @type ="Epica"
                    elsif type == "4"
                        @type = "Legendaria"
                    end 
                restype = typedisponible.include? @type
                    if restype == true 
                        ClashRoyale.coste
                    else 
                        puts "Lo Siento esa calidad no esta disponible :c ".rjust 300
                        ClashRoyale.type
                    end                            
            end 
            
            def self.coste
                puts "\nIngresa el coste de la  carta: " + @name 
                puts "coste: "
                @coste = gets.chomp
                    if /[0-9]/.match (@coste)                                       
                        ClashRoyale.target                        
                    else
                        puts "Lo siento Es un coste que no concibo :o ".rjust 300 
                        ClashRoyale.coste
                    end                                 
            end 

            def self.target
                puts "\nIngresa su Objetivo de Ataque:  "
                attackdisponible = ["Aereo","Tierra", "Tierra y Aereo"]
                puts "Tipo de Ataque: "
                puts "1.-Aereo", "2.-Tierra", "3.-Tierra y Aereo"
                attack = gets.chomp.capitalize
                    if attack == "1"
                        @attack = "Aereo"
                    elsif
                        attack == "2"
                        @attack = "Tierra"
                    elsif
                        attack == "3"
                        @attack = "Tierra y Aereo"
                    end 
                resattack = attackdisponible.include? @attack
                    if resattack == true                                  
                        ClashRoyale.speed
                    else 
                        puts "\nLo siento la carta no esta en su rango de ataque "
                        ClashRoyale.target
                    end                       
            end 
            
            def self.speed 
                puts "ingresa la velocidad de ataque de la carta: " + @name
                puts "Velocidad de Ataque: (Seg)"
                @speed = gets.chomp
                    if /[0-9]/.match (@speed)                    
                    ClashRoyale.level            
                    else 
                        puts "\nLo siento no reonozco la velocidad "
                        ClashRoyale.speed                    
                    end               
            end 

            def self.level
                puts "\nIngresa el nivel max"
                @level = gets.chomp
                    if /[0-9]/.match (@level)
                        ClashRoyale.printtxt
                    else 
                        puts "\nLo siento el nivel es insostenible "
                        ClashRoyale.level
                    end 
            end 

            def self.printtxt
                archivo = File.new("Cartas.Clash", "a")
                archivo.puts (@name.ljust(22) + @type.ljust(13)+ @coste.ljust(10) + @attack.ljust(22)+ @speed+" seg ".ljust(18)+ @level.ljust(10))
                archivo.close
                ClashRoyale.add       
            end                                         

    def self.add
        puts "quieres agregar mas contenido? s/n"
        add= gets.chomp
        if add == "s"
            ClashRoyale.opcion2
        elsif add == "n"
        ClashRoyale.menu
        else "No entendi eso"
            ClashRoyale.add
        end 
    end 

    def self.opcion3        
        str= "Ingresa Busqueda: "
        puts str.rjust  300

        @busqueda = gets.chomp.capitalize 
        File.open('Cartas.Clash', 'r') do |f1|
            while linea = f1.gets 
             
            @linea = linea.split(' ')   
            @lineacompleta = linea                     
            @resbusqueda =  @linea.include? @busqueda
            if @resbusqueda == true 
                
                
                puts  @lineacompleta  
                @match = 1
            end
            end                       
          end
            if @match != 1
                puts "lo siento no encontre un Resultado"
            end 
        ClashRoyale.consulta
    
    end 

    def self.consulta
        puts "\n Quieres hacer otra consulta? s/n "
        consulta = gets.chomp
                     if consulta == "s"
                        ClashRoyale.opcion3
                     elsif
                        consulta == "n"
                        ClashRoyale.menu
                     else puts "error no reconozco el comando"
                        ClashRoyale.consulta
                     end 
    end 

    def self.opcion4
        str = "Eliminar Registro"
        puts str.rjust 300               
        require 'fileutils'      
        
        content = File.readlines 'Cartas.Clash'
        contenido = IO.readlines('Cartas.Clash')          
        puts contenido    

        puts "\nIngresa la Carta que deseas Eliminar "
        delete = gets.chomp.capitalize

            open('Cartas.Clash', 'r') do |f|
            open('file.txt.tmp', 'w') do |f2|
                f.each_line do |line|
                f2.write(line) unless line.start_with? delete
                end
            end
            end
            FileUtils.mv 'file.txt.tmp', 'Cartas.Clash'

            content = File.readlines 'Cartas.Clash'
     contenido = IO.readlines('Cartas.Clash')
     puts contenido               
        ClashRoyale.menu
    

        ClashRoyale.menu
    end 

    def self.opcion5
        str = "Eliminar todos los Registros "
        puts str.rjust 300
        
        File.open('Cartas.Clash', 'w') do |f2|
            # '\n' es el retorno de carro
            fila = "nombre:".ljust(22) + "Tipo:".ljust(13) + "Coste:".ljust(10) + "Tipo de ataque".ljust(22) + "Velocidad".ljust(18) + "Nivel Max".ljust(10) 
            f2.puts fila 
            f2.puts 
          end

        ClashRoyale.menu
    end 

    def self.opcion6
        str = "Ordenar los Registros"
        puts str.rjust 300 

        File.open("out.txt", "w") do |file|
            File.readlines("Cartas.Clash").sort.each do |line|
              file.write(line.chomp<<"\n")
          end
        end

        content = File.readlines 'out.txt'
            
             contenido = IO.readlines('out.txt')
             puts contenido               
                ClashRoyale.menu
    end         
end

ClashRoyale.menu
