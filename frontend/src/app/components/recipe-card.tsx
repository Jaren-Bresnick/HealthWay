import Button from '@mui/joy/Button';
import CircularProgress from '@mui/joy/CircularProgress';

interface RecipeCardProps {
    image_link: string;
    title: string;
    domain: string;
    calories: number;
    carbs: number;
    fat: number;
    protein: number;
    link: string;
}

export default function RecipeCard({
    image_link,
    title,
    domain,
    calories,
    carbs,
    fat,
    protein,
    link,
}: RecipeCardProps) {
    return (
        <div className='border rounded-md p-3'>

            <div className='grid grid-cols-1 md:grid-cols-5 gap-4'>

                <img
                    src={image_link}
                    alt="Picture of the food"
                    width={300}
                    height={200}
                    className='col-span-2 rounded-md object-cover w-full h-full max-h-32 md:max-h-full'
                />

                <div className='col-span-1 md:col-span-3 flex flex-col justify-between space-y-3'>

                    <div className='flex flex-col'>
                        <p className='font-bold text-xl'>{title}</p>
                        <p className='text-slate-500'>From: {domain}</p>
                    </div>

                    <div className='grid grid-cols-4'>

                        <div className='flex flex-col items-center'>
                            <CircularProgress size="lg" value={15} determinate color='success'>
                                <p className='font-black'>{calories}</p>
                            </CircularProgress>
                            <p className='text-slate-500'>Calories</p>
                        </div>


                        <div className='flex flex-col items-center'>
                            <CircularProgress size="lg" value={15} determinate color='danger'>
                                <p className='font-black'>{carbs}g</p>
                            </CircularProgress>
                            <p className='text-slate-500'>Carbs</p>
                        </div>

                        <div className='flex flex-col items-center'>
                            <CircularProgress size="lg" value={20} determinate>
                                <p className='font-black'>{fat}g</p>
                            </CircularProgress>
                            <p className='text-slate-500'>Fat</p>
                        </div>

                        <div className='flex flex-col items-center'>
                            <CircularProgress size="lg" value={39} determinate color='neutral'>
                                <p className='font-black'>{protein}g</p>
                            </CircularProgress>
                            <p className='text-slate-500'>Protein</p>
                        </div>

                    </div>

                    <Button variant="outlined" color="neutral" className='w-full' component="a" href={link}>View Recipe</Button>

                </div>

            </div>
        </div>
    );
}
