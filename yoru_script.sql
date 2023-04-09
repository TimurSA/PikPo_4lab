
create table source_files (
	id integer PRIMARY KEY autoincrement,
	filename varchar(255) NOT NULL,
	processed datetime
);

create table processed_data_doctor (
	doctor_id integer PRIMARY KEY NOT NULL,
	firstname varchar(255) NOT NULL,
	lastname varchar(255) NOT NULL,
	specialization varchar(255) NOT NULL,
	contact_info varchar(255),
	source_file integer NOT NULL,
	CONSTRAINT fk_source_files
	FOREIGN KEY (source_file)
	REFERENCES source_files(id)
	ON DELETE CASCADE
);

create table processed_data_patient (
	patient_id integer PRIMARY KEY NOT NULL,
	firstname varchar(255) NOT NULL,
	lastname varchar(255) NOT NULL,
	source_file integer NOT NULL,
	CONSTRAINT fk_source_files
	FOREIGN KEY (source_file)
	REFERENCES source_files(id)
	ON DELETE CASCADE
);

create table processed_data_appointment (
	appointment_id integer PRIMARY KEY autoincrement,
	doctor_id integer NOT NULL,
	patient_id integer NOT NULL,
	date_time date,
	source_file integer NOT NULL,
	CONSTRAINT fk_source_files
	FOREIGN KEY (source_file)
	REFERENCES source_files(id)
	ON DELETE CASCADE,
	CONSTRAINT fk_processed_data_patient FOREIGN KEY(patient_id) REFERENCES processed_data_patient(patient_id) ON DELETE CASCADE,
	CONSTRAINT fk_processed_data_doctor FOREIGN KEY(doctor_id) REFERENCES processed_data_doctor(doctor_id)
	ON DELETE CASCADE
);