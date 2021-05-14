class Building
  attr_accessor :name, :address

  def initialize(name, address)
    @name = name
    @address = address
  end

  def get_description
    puts "Name: #{self.name}\nAddress: #{self.address}"
  end
end

class ApartmentBuilding < Building
  def initialize()
    super()
  end
end


building = ApartmentBuilding.new("Empire State Building", "an address")
building.get_description
