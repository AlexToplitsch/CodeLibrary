var faker = require('faker/locale/de_AT');
let database = {user:[], costumer:[], supplier:[], employee:[]};
const anzahl = 1000;

for(let i = 1; i <= anzahl; i++){
    database.user.push({
        id: i,
        name: faker.name.firstName() + " " + faker.name.lastName(),
        phone: faker.phone.phoneNumber(),
        userNamer: faker.internet.userName(),
        email: faker.internet.email(),
        address: faker.address.city() + ", " + faker.address.country()
    });
}

for(let i = 1; i <= anzahl; i++){
    database.costumer.push({
        id: i,
        name: faker.company.companyName(),
        about: faker.lorem.paragraph(),
        phone: faker.phone.phoneNumber(),
        email: faker.internet.email(),
        adress: faker.address.city() + ", " + faker. address.country()
    });
}

for(let i = 1; i <= anzahl; i++){
    database.supplier.push({
        id: i,
        companyName: faker.company.companyName(),
        about: faker.lorem.paragraph(),
        phone: faker.phone.phoneNumber(),
        email: faker.internet.email(),
        address: faker.address.city() + ", " + faker.address.country()
    });
}

for(let i = 1; i <= anzahl; i++){
    database.employee.push({
        id: i,
        name: faker.name.firstName() + " " + faker.name.lastName(),
        entryDate: faker.date.recent(),
        job: faker.name.jobTitle(),
        phone: faker.phone.phoneNumber(),
        email: faker.internet.email(),
        salary: "€" + faker.finance.amount() + "M",
        address: {
            city: faker.address.city(),
            state: faker.address.state(),
            country: faker.address.country()
            }
    });
}
console.log(JSON.stringify(database));