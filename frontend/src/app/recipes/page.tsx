'use client'

import RecipeCard from '../components/recipe-card';
import { useEffect, useState } from 'react';

export default function Home() {
  
  const [data, setdata] = useState(null)

  useEffect(() => {
    fetch('http://127.0.0.1:8000/inventory/get_recipes/abc')
      .then(response => response.json())
      .then(data => setdata(data));
  }, []);

 
  return (
    <div className='flex flex-row justify-center'>

      <div className='m-10 flex flex-col space-y-4 max-w-[1100px]'>

        <div className='flex flex-col'>
          <p className='font-bold text-2xl'>Recipes made for Shrisha</p>
          <p className='text-slate-500'>Here are a list of curated recipies for you. These recipies are made to match your dietary preferences and fitness goals while ensuring minimal food waste, giving you real food you can make with the things you have in your kitchen right now.</p>
        </div>

        <div className='grid grid-cols-1 lg:grid-cols-2 gap-3'>
          {data && data.map((recipe, index) => (
            <RecipeCard 
              key={index} 
              title={recipe.title}
              image_link={recipe.img_url}
              domain={recipe.domain}
              nutrition={recipe.nutrition}
              link={recipe.link}
            />
          ))}
        </div>
      </div>
    </div>

  );
}
