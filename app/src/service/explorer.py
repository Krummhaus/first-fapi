from model.explorer import Explorer
import fake.explorer as data


def get_all() -> list[Explorer]:
    return data.get_all()
