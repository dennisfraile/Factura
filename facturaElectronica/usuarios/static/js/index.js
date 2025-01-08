let dataTableRole;
let dataTableUser;
let dataTableUserIsInitialized = false;
let dataTableRoleIsInitialized = false;

const dataTableRoleOptions = {
    column: [
        { className: "centered", targets: [0, 1] },
        { orderable: false, targets: [1] },
        { searchable: false, targets: [1] }
    ],
    pageLength: 6,
    destroy: true
};

const dataTableUserOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
        { orderable: false, targets: [5,6] },
        { searchable: false, targets: [3,4,5,6] }
    ],
    pageLength: 6,
    destroy: true
};

const initDataTableRole = async () => {
    if (dataTableRoleIsInitialized) {
        dataTableRole.destroy();
    }
    dataTableRole = $("#table-role").DataTable(dataTableRoleOptions);
    dataTableRoleIsInitialized = true;
};

const initDataTableUser = async () => {
    if (dataTableUserIsInitialized) {
        dataTableUser.destroy();
    }
    dataTableUser = $("#table-user").DataTable(dataTableUserOptions);
    dataTableUserIsInitialized = true;
};