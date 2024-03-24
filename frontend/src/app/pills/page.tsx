import React from 'react';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import moment from 'moment';
import PrescriptionCard from '../components/pills-card';



const capitalizeEachWord = (str: string): string => {
  return str.replace(/\b\w/g, (char) => char.toUpperCase());
};

export default function Home() {
  const startOfWeek = moment().startOf('week');
  const days = Array.from(Array(7).keys()).map((day) =>
    moment(startOfWeek).add(day, 'days')
  );


  
  const prescriptionItems = [
    {
      name: "GENERIC MEDICATION",
      dose_size: "2 tablets",
      pill_count: 180,
      refill_date: null,
      expiry_date: "2/16",
      description_of_medication: "No additional instructions", // Assuming a default value for demonstration
      pills_used_per_day: 6,
      imageUrl: "pill.jpg"
    }, 
    {
      name: "GENERIC MEDICATION",
      dose_size: "2 tablets",
      pill_count: 180,
      refill_date: null,
      expiry_date: "2/16",
      description_of_medication: "No additional instructions", // Assuming a default value for demonstration
      pills_used_per_day: 6,
      imageUrl: "pill.jpg"
    }, 
    {
      name: "GENERIC MEDICATION",
      dose_size: "2 tablets",
      pill_count: 180,
      refill_date: null,
      expiry_date: "2/16",
      description_of_medication: "No additional instructions", // Assuming a default value for demonstration
      pills_used_per_day: 6,
      imageUrl: "pill.jpg"
    }, 
    {
      name: "GENERIC MEDICATION",
      dose_size: "2 tablets",
      pill_count: 180,
      refill_date: null,
      expiry_date: "2/16",
      description_of_medication: "No additional instructions", // Assuming a default value for demonstration
      pills_used_per_day: 6,
      imageUrl: "pill.jpg"
    }, 
  
    
    // Additional prescription items can be added here
  ];

  const isToday = (date: moment.Moment): boolean => {
    return moment().isSame(date, 'day');
  };

  return (
    <div className='flex flex-row justify-center'>
      <div className='m-12 flex flex-col space-y-4 max-w-[1100px]'>
        <div className='flex flex-col text-start'>
          <Typography variant="h5" className='font-bold'>Weekly Pills Schedule</Typography>
          <Typography variant="body1" className='text-slate-500'>
            Today is {moment().format('dddd')}. Here is a list of pills you should take today. Please review them carefully.
          </Typography>
        </div>
        <Grid container spacing={4}>
  {days.map((date, index) => (
    <Grid item key={index} xs={12} sm={6} md={4} lg={true} style={{
      border: '1px solid #ccc',
      borderRadius: '8px',
      padding: '8px',
      margin: '2px',
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
          {prescriptionItems
            .filter(item => item.pills_used_per_day > 1)
            .map(item => capitalizeEachWord(item.name.toLowerCase()))
            .join(', ')
          }
        </Typography>
      </div>
    </Grid>
  ))}
</Grid>


        <div className='flex flex-col mt-12' >
          <Typography variant="h5" className='font-bold'>Current Medications</Typography>
          <Typography variant="body1" className='text-slate-500'>
            Here are the details of your current medications. Please review them carefully.
          </Typography>
        </div>
        <div className='grid grid-cols-1 lg:grid-cols-2 gap-1'>
          {prescriptionItems.map((item, index) => (
            <PrescriptionCard
              key={index}
              name={item.name}
              dose_size={item.dose_size}
              pill_count={item.pill_count} // Keeping as number based on updated PrescriptionCardProps
              refill_date={item.refill_date}
              expiry_date={item.expiry_date}
              pills_used_per_day={item.pills_used_per_day} // Keeping as number
              description_of_medication={item.description_of_medication} // Directly passing the value
              imageUrl={item.imageUrl}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
