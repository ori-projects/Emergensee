export class PatientModule { 
  public description: string;
  public imagePath: string;
  public image: string;
  public name: string;
  public email: string;
  public phoneNumber: string;
  public age: string;
  public bloodPressure: string;
  public bloodSugar: string;
  public procedureCount: string;
  public infectionsReported: string;
  public bodyTemperature: string;
  public heartRate: string;
  public operativeProcedure: string;
  public feelingsAndUrge: string;
  public disease: string;
  public criticalFeelings: string;

  constructor(description :string,
     imagePath: string,
     image: string,
     name: string,
     email: string,
     phoneNumber: string,
     age: string,
     bloodPressure: string,
     bloodSugar: string,
     procedureCount: string,
     infectionsReported: string,
     bodyTemperature: string,
     heartRate: string,
     operativeProcedure: string,
     feelingsAndUrge: string,
     disease: string,
     criticalFeelings: string) {
    this.description = description;
    this.imagePath = imagePath;
    this.image = image;
    this.name = name;
    this.email = email;
    this.phoneNumber = phoneNumber;
    this.age = age;
    this.bloodPressure = bloodPressure;
    this.bloodSugar = bloodSugar;
    this.procedureCount = procedureCount;
    this.infectionsReported = infectionsReported;
    this.bodyTemperature = bodyTemperature;
    this.heartRate = heartRate;
    this.operativeProcedure = operativeProcedure;
    this.feelingsAndUrge = feelingsAndUrge;
    this.disease = disease;
    this.criticalFeelings = criticalFeelings;
  }
}