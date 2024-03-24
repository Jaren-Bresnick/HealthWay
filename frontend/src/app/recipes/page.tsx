import RecipeCard from '../components/recipe-card';

export default function Home() {
  return (
    <div className='flex flex-row justify-center'>

      <div className='m-10 flex flex-col space-y-4 max-w-[1100px]'>

        <div className='flex flex-col'>
          <p className='font-bold text-2xl'>Recipies made for Daniel</p>
          <p className='text-slate-500'>Here are a list of curated recipies for you. These recipies are made to match your dietary preferences and fitness goals while ensuring minimal food waste, giving you real food you can make with the things you have in your kitchen right now.</p>
        </div>

        <div className='grid grid-cols-1 lg:grid-cols-2 gap-3'>
          <RecipeCard
            image_link="https://i2.supercook.com/c/1/9/3/c19335ce2bc248a247db3af3ac6dc4bd-0.jpg"
            title="Mom's Classic Monkey Bread"
            domain="allrecipes.com"
            calories={200}
            carbs={23}
            fat={10}
            protein={6}
            link="https://www.allrecipes.com/recipe/21461/moms-classic-monkey-bread/"
          />
           <RecipeCard
            image_link="https://i2.supercook.com/c/1/9/3/c19335ce2bc248a247db3af3ac6dc4bd-0.jpg"
            title="Mom's Classic Monkey Bread"
            domain="allrecipes.com"
            calories={200}
            carbs={23}
            fat={10}
            protein={6}
            link="https://www.allrecipes.com/recipe/21461/moms-classic-monkey-bread/"
          />
          <RecipeCard
            image_link="https://i2.supercook.com/3/c/b/6/3cb6804cb84ab0735988d1e8ada81607-0.jpg"
            title="Classic Nachos"
            domain="sidechef.com"
            calories={270}
            carbs={10}
            fat={15}
            protein={4}
            link="https://www.allrecipes.com/recipe/21461/moms-classic-monkey-bread/"
          />
           <RecipeCard
            image_link="https://i2.supercook.com/c/1/9/3/c19335ce2bc248a247db3af3ac6dc4bd-0.jpg"
            title="Mom's Classic Monkey Bread"
            domain="allrecipes.com"
            calories={200}
            carbs={23}
            fat={10}
            protein={6}
            link="https://www.allrecipes.com/recipe/21461/moms-classic-monkey-bread/"
          />
          <RecipeCard
            image_link="https://i2.supercook.com/a/9/6/c/a96c386123c29ad21c828951d62eec82-0.jpg"
            title="Fruit Jam"
            domain="recipeland.com"
            calories={420}
            carbs={20}
            fat={5}
            protein={2}
            link="https://www.allrecipes.com/recipe/21461/moms-classic-monkey-bread/"
          />
         
          <RecipeCard
            image_link="https://i2.supercook.com/c/1/9/3/c19335ce2bc248a247db3af3ac6dc4bd-0.jpg"
            title="Mom's Classic Monkey Bread"
            domain="allrecipes.com"
            calories={200}
            carbs={23}
            fat={10}
            protein={6}
            link="https://www.allrecipes.com/recipe/21461/moms-classic-monkey-bread/"
          />
          <RecipeCard
            image_link="https://i2.supercook.com/c/1/9/3/c19335ce2bc248a247db3af3ac6dc4bd-0.jpg"
            title="Mom's Classic Monkey Bread"
            domain="allrecipes.com"
            calories={200}
            carbs={23}
            fat={10}
            protein={6}
            link="https://www.allrecipes.com/recipe/21461/moms-classic-monkey-bread/"
          />
        </div>
      </div>
    </div>

  );
}
