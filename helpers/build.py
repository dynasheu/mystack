from os import path, listdir, makedirs, walk
import yaml
import shutil

# helper functions
def read_template(template_name):
    file_name = path.join('templates', f'{template_name}.yaml')
    with open(file_name, 'r') as file:
        data = file.read()
    return data

def create_folders(container):
    file_name = path.join('templates', f'{container}.yaml')
    with open(file_name, 'r') as file:
        data = yaml.load(file, Loader=yaml.Loader)
    
    try:
        volumes = data[next(iter(data))]['volumes']
        for volume in volumes:
            volume_list = volume.split(':')[0].split('/')
            if '.' in volume_list[-1]:
                volume_list.pop()
            if volume_list[1] == 'containers':
                create_path = path.join(*volume_list)
                makedirs(create_path, exist_ok=True)
    except Exception as e:
        pass
    
    temp_folder = path.join('templates', container)
    if path.isdir(temp_folder):
        print(temp_folder)
        dest_folder = path.join('containers', container)
        shutil.copytree(temp_folder, dest_folder, dirs_exist_ok=True)

def build_docker_compose(selected_containers):
    compose_output = '# docker-compose.yaml \nversion: \'3.9\'\n\nservices:\n'

    for container in selected_containers:
        create_folders(container)
        compose_output += read_template(container)
    
    with open('docker-compose.yaml', 'w') as file:
        file.write(compose_output)

def check_selection():
    selected_file_name = path.join('templates', 'selected_containers')
    if path.exists(selected_file_name):
        with open(selected_file_name, 'r') as file:
            data = file.readlines()
        return [item.strip() for item in data]
    else:
        return []

def write_selection(selected_containers):
    selected_file_name = path.join('templates', 'selected_containers')
    with open(selected_file_name, 'w') as file:
        file.writelines([f'{item}\n' for item in selected_containers])


def main():
    print('\"docker-compose.yaml\" builder!')

    # run available containers
    available_containers = [item.replace('.yaml', '') for item in listdir('templates') if item.endswith('.yaml')]

    # check old selection
    old_selected_containers = check_selection()

    # container selection
    print('Select containers (y/n/s):')
    selected_containers = []
    for container in available_containers:
        selection = input(f' - {container}: ')
        if selection == 'y':
            selected_containers.append(container)
        elif selection == 's' and container in old_selected_containers:
            selected_containers.append(container)
    
    # build docker-compose or not
    if len(selected_containers) > 0:
        print('\nBuilding \'docker-compose.yaml\' for:')
        print(', '.join(selected_containers))
        build_docker_compose(selected_containers)

        print('\nUse command to start docker:\ndocker-compose up -d')
        write_selection(selected_containers)
    else:
        print('\nNo container selected!')

    

if __name__ == '__main__':
    main()
