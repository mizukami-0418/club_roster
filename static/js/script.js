// script.js

let options = {
    valueNames: [
        'name', 'team', 'field_position', 'batting_average', 'homerun', 'height', 'weight', 'birth_date'
    ]
};

let sortableTable = new List('sortableTable', options);

let options2 = {
    valueNames: [
        'name', 'team', 'position', 'earned_run_average', 'height', 'weight', 'birth_date'
    ]
};

let sortableTable2 = new List('sortableTable2', options2);
