import React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';

interface PrescriptionCardProps {
    name: string;
    dose_size: string;
    pill_count: number; // Note the updated type here
    refill_date: string | null;
    expiry_date: string;
    pills_used_per_day: number; // Note the updated type here
    description_of_medication: string;
    imageUrl: string;
}

export default function PrescriptionCard({
    name,
    dose_size,
    pill_count,
    refill_date,
    expiry_date,
    pills_used_per_day,
    description_of_medication,
    imageUrl,
}: PrescriptionCardProps) {
    return (
        <Card className='max-w-xl mx-auto my-2 border'>
            <div className='flex flex-col md:flex-row'>
                <CardMedia
                    component="img"
                    image={imageUrl}
                    alt={`${name} medication`}
                    className="w-full md:w-48"
                />
                <CardContent className='flex flex-col justify-between'>
                    <Typography gutterBottom variant="h5" component="div" className='font-bold'>
                        {name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        Dosage: {dose_size}
                    </Typography>
                    <div className='my-3'>
                        <Typography variant="body2" component="p">
                            Quantity: {pill_count}
                        </Typography>
                        <Typography variant="body2" component="p">
                            Refill Date: {refill_date ?? 'N/A'}
                        </Typography>
                        <Typography variant="body2" component="p">
                            Expiration Date: {expiry_date}
                        </Typography>
                        <Typography variant="body2" component="p">
                            Daily Usage: {pills_used_per_day} pills
                        </Typography>
                    </div>
                    {description_of_medication && (
                        <Typography variant="body2" color="text.secondary">
                            Description: {description_of_medication}
                        </Typography>
                    )}
                </CardContent>
            </div>
        </Card>
    );
}
