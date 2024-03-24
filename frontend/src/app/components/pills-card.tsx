import React from 'react';
import Button from '@mui/joy/Button'; // Assuming you'll use it later as it's imported
import Typography from '@mui/material/Typography';

interface PrescriptionCardProps {
    name: string;
    dosage: string;
    quantity: string;
    refills: string;
    expiration_date: string;
    imageUrl: string; // Added imageUrl property
}

export default function PrescriptionCard({
    name,
    dosage,
    quantity,
    refills,
    expiration_date,
    imageUrl, // Added this parameter to function
}: PrescriptionCardProps) {
    return (
        <div className='border rounded-md p-3'>
            <div className='grid grid-cols-1 md:grid-cols-5 gap-4'>
                {/* Updated to display medication image */}
                <div className='col-span-2 rounded-md overflow-hidden flex justify-center items-center'>
                    <img src={imageUrl} alt={`${name} medication`} className="max-w-full max-h-full" />
                </div>
                <div className='col-span-1 md:col-span-3 flex flex-col justify-between space-y-3'>
                    <div className='flex flex-col'>
                        <p className='font-bold text-xl'>{name}</p>
                        <p className='text-slate-500'>{dosage}</p>
                    </div>
                    <div className='grid grid-cols-2 gap-4'>
                        <div className='flex flex-col items-center'>
                            <Typography variant="h6" component="div">{quantity}</Typography>
                            <p className='text-slate-500'>Quantity</p>
                        </div>
                        <div className='flex flex-col items-center'>
                            <Typography variant="h6" component="div">{refills}</Typography>
                            <p className='text-slate-500'>Refills</p>
                        </div>
                    </div>
                    <div>
                        <p className='font-bold'>Expiration Date: {expiration_date}</p>
                    </div>
                </div>
            </div>
        </div>
    );
}
