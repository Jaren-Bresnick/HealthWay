import React from 'react';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import moment from 'moment';
import PrescriptionCard from '../components/pills-card';

export default function Home() {
  const startOfWeek = moment().startOf('week');
  const days = Array.from(Array(7).keys()).map((day) =>
    moment(startOfWeek).add(day, 'days')
  );

  const prescriptions = [
    {
      name: "GENERIC MEDICATION A",
      dosage: "TAKE TWO TABLETS BY MOUTH THREE TIMES DAILY",
      quantity: "60",
      refills: "2 REFILLS",
      expiration_date: "2023-12-31",
      imageUrl: "pill.jpg"
    },
    {
      name: "GENERIC MEDICATION B",
      dosage: "APPLY TOPICALLY TWICE DAILY",
      quantity: "1 Tube",
      refills: "NO REFILLS",
      expiration_date: "2024-01-15",
      imageUrl: "pill.jpg"
    },
    {
      name: "GENERIC MEDICATION C",
      dosage: "TAKE TWO TABLETS BY MOUTH THREE TIMES DAILY",
      quantity: "60",
      refills: "2 REFILLS",
      expiration_date: "2023-12-31",
      imageUrl: "pill.jpg"
    },
    {
      name: "GENERIC MEDICATION D",
      dosage: "APPLY TOPICALLY TWICE DAILY",
      quantity: "1 Tube",
      refills: "NO REFILLS",
      expiration_date: "2024-01-15",
      imageUrl: "pill.jpg"
    },

    // More prescriptions can be added here
  ];

  // Method to determine if the day is today
  const isToday = (date: moment.Moment): boolean => {
    return moment().isSame(date, 'day');
  };

  return (
    <div className='flex flex-row justify-center'>
      <div className='m-10 flex flex-col space-y-10 max-w-[1100px]'>
        {/* Weekly Schedule */}
        <div className='flex flex-col text-start'>
          <Typography variant="h5" className='font-bold'>Weekly Pills Schedule</Typography>
          <Typography variant="body1" className='text-slate-500'>
            Today is {moment().format('dddd')}. Here is a list of pills you should take today. Please review them carefully.
          </Typography>
        </div>
        <Grid container spacing={2}>
          {days.map((date, index) => (
            <Grid item key={index} xs={12} sm={6} md={4} lg={true} style={{
              border: '1px solid #ccc',
              borderRadius: '8px',
              padding: '8px',
              display: 'flex',
              flexDirection: 'column',
              height: '150px',
              backgroundColor: isToday(date) ? '#add8e6' : '#ffffff',
            }}>
              <div style={{ marginBottom: 'auto' }}>
                <Typography variant="subtitle1" style={{ fontWeight: 'bold', textAlign: 'center' }}>
                  {date.format('dddd')}
                </Typography>
                <Typography variant="body2" style={{ textAlign: 'center' }}>
                  {date.format('MMM D')}
                </Typography>
              </div>
              <div style={{ marginTop: 'auto', textAlign: 'center' }}>
                <Typography variant="body2" style={{ opacity: 0.7 }}>
                  Pills list...
                </Typography>
              </div>
            </Grid>
          ))}
        </Grid>

        {/* Prescriptions Section */}
        <div className='flex flex-col mt-10'>
          <Typography variant="h5" className='font-bold'>Current Medications</Typography>
          <Typography variant="body1" className='text-slate-500'>
            Here are the details of your current medications. Please review them carefully.
          </Typography>
        </div>
        <div className='grid grid-cols-1 lg:grid-cols-2 gap-4'>
          {prescriptions.map((prescription, index) => (
            <PrescriptionCard
              key={index}
              name={prescription.name}
              dosage={prescription.dosage}
              quantity={prescription.quantity}
              refills={prescription.refills}
              expiration_date={prescription.expiration_date}
              imageUrl={prescription.imageUrl} // Passing the imageUrl prop
            />
          ))}
        </div>
      </div>
    </div>
  );
}
