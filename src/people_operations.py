import json
import os
from datetime import datetime


class PersonDatabase:
    def __init__(self, filename="database/people_database.json"):
        self.filename = filename
        self.data = self._load_database()
        self._save_database()

    def _load_database(self):
        """Load database from file or create new one"""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        else:
            return {"people": {}}

    def _save_database(self):
        """Save current state to file"""
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_person(self, cpf, name, birth_date, **kwargs):
        """Add a new person to the database"""
        if cpf in self.data["people"]:
            print(f"CPF {cpf} already exists in database")
            # raise ValueError(f"CPF {cpf} already exists in database")
            return

        person_data = {
            "name": name,
            "cpf": cpf,
            "birth_date": birth_date,
            "last_seen": datetime.now().isoformat(),
            "last_procedure_id": 0,
            "procedures": {},
            **kwargs,
        }

        self.data["people"][cpf] = person_data
        self._save_database()
        return True

    def add_dental_procedure(self, cpf, date, procedures, notes="", **kwargs):
        """Add a new dental procedure to the database"""
        if cpf not in self.data["people"]:
            return
        procedure_id = f"{int(self.data["people"][cpf].get("last_procedure_id", 0)) +1}"
        dental_data = {"date": date, "procedures": procedures, "notes": notes, **kwargs}

        self.data["people"][cpf]["procedures"][procedure_id] = dental_data
        self.data["people"][cpf]["last_procedure_id"] = procedure_id
        self._save_database()
        return True

    def update_person(self, cpf, **kwargs):
        """Update existing person's information"""
        if cpf not in self.data["people"]:
            raise KeyError(f"CPF {cpf} not found in database")

        person = self.data["people"][cpf]
        for key, value in kwargs.items():
            person[key] = value
        person["last_seen"] = datetime.now().isoformat()

        self._save_database()
        return True

    def update_dental_procedure(self, cpf, procedure_id, **kwargs):
        """Update existing dental_procedure's information"""
        if cpf not in self.data["people"]:
            raise KeyError(f"cpf {cpf} not found in database")

        if procedure_id not in self.data["people"][cpf]["procedures"].keys():
            raise KeyError(f"procedure_id {procedure_id} not found in database")

        dental_data = self.data["people"][cpf]["procedures"][procedure_id]
        for key, value in kwargs.items():
            dental_data[key] = value

        self._save_database()
        return True
    

    def get_person(self, cpf):
        """Retrieve a person's data by CPF"""
        return self.data["people"].get(cpf, None)

    def get_all_people(self):
        """Get list of all people in database"""
        return list(self.data["people"].values())

    def get_all_people_cpfs(self):
        """Get list of all people in database"""
        return list(self.data["people"].keys())

    def get_all_people_names(self):
        """Get list of all people in database"""
        simple_dict = {}
        for cpf in list(self.data["people"].keys()):
            simple_dict[self.data["people"][cpf]["name"]] = cpf
        return simple_dict

    def get_dental_procedure(self, cpf, procedure_id):
        """Retrieve a dental_procedure's data by CPF"""
        if cpf not in self.data["people"]:
            raise KeyError(f"cpf {cpf} not found in database")
        return self.data["people"][cpf]["procedures"].get(procedure_id, None)
    
    def get_person_dental_procedures(self, cpf):
        """Get list of all dental_procedure for person"""
        return list(self.data["people"][cpf]["procedures"].values())

    def get_person_dental_procedures_id(self, cpf):
        """Get list of all dental_procedure for person"""
        return list(self.data["people"][cpf]["procedures"].keys())
    
    def get_dental_operations(self, cpf):
        """Retrieve a dental_procedure's data by CPF"""
        if cpf not in self.data["people"]:
            raise KeyError(f"cpf {cpf} not found in database")
        return self.data["people"][cpf]["procedures"].get("procedures", {})
    
    def get_dental_operations_on_tooth(self, cpf, procedure_id, tooth_id):
        """Retrieve a dental_procedure's data by CPF"""
        if cpf not in self.data["people"]:
            raise KeyError(f"cpf {cpf} not found in database")
        return self.data["people"][cpf]["procedures"][procedure_id]["procedures"].get(tooth_id, [])

    def delete_person(self, cpf):
        """Remove a person from the database"""
        if cpf not in self.data["people"]:
            raise KeyError(f"CPF {cpf} not found in database")

        del self.data["people"][cpf]
        self._save_database()
        return True

    def delete_dental_procedure(self, cpf, procedure_id):
        """Remove a dental_procedure from the database"""
        if cpf not in self.data["people"]:
            raise KeyError(f"CPF {cpf} not found in database")
        if procedure_id not in self.data["people"][cpf]["procedures"]:
            print(self.data["people"][cpf]["procedures"])
            raise KeyError(f"procedure_id {procedure_id} not found in database")

        del self.data["people"][cpf]["procedures"][procedure_id]
        self._save_database()
        return True

    def search(self, **kwargs):
        """Search for people matching given criteria"""
        results = []
        for person in self.data["people"].values():
            match = True
            for key, value in kwargs.items():
                if person.get(key) != value:
                    match = False
                    break
            if match:
                results.append(person)
        return results


# Example usage
if __name__ == "__main__":
    db = PersonDatabase()

    # Add new person
    db.add_person(
        cpf="12345678900",
        name="John Doe",
        birth_date="1990-01-01",
        phone="+5511999999999",
    )

    # Update person
    db.update_person("12345678900", phone="+5511999999999")

    # Get person
    person = db.get_person("12345678900")
    print("Retrieved person:", person)

    # Search example
    results = db.search(name="Johnathan Doe")
    print("Search results:", results)

    # List all
    # all_people = db.list_all_people()
    # print("All entries:", all_people)
